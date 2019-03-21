import datetime
import json
import logging
import time
from typing import Optional


def getLogger(name: Optional[str] = None,
              level: str='INFO',
              fmt: str='text') -> logging.Logger:
    logger: logging.Logger = logging.getLogger(name)
    for handler in logger.handlers:
        logger.removeHandler(handler)

    handler = logging.StreamHandler()
    if fmt.lower() == 'json':
        handler.setFormatter(JsonIsoFormatter(
            ['asctime', 'levelname', 'message', 'name']))
    else:
        handler.setFormatter(IsoFormatter(
            '%(asctime)s [%(levelname)s] %(message)s'))

    logger.addHandler(handler)
    logger.setLevel(getattr(logging, level.upper()))
    return logger


class IsoFormatter(logging.Formatter):
    class TzInfo(datetime.tzinfo):
        def utcoffset(self, dt):
            return -datetime.timedelta(seconds=time.timezone)

        def dst(self, dt):
            return datetime.timedelta(0)

        def tzname(self, dt):
            return time.tzname

    def formatTime(self, record, datefmt=None):
        dt = datetime.datetime.fromtimestamp(record.created, self.TzInfo())
        return dt.strftime(datefmt) if datefmt \
            else dt.replace(microsecond=0).isoformat()


class JsonIsoFormatter(IsoFormatter):
    def __init__(self, fields=[], datefmt=None, encoder=None):
        logging.Formatter.__init__(self, None, datefmt)
        self.fields = fields
        self.encoder = encoder

    def format(self, record):
        data = {'msg': record.msg}
        if 'asctime' in self.fields:
            record.asctime = self.formatTime(record, self.datefmt)

        for field in self.fields:
            data[field] = getattr(record, field)

        if 'asctime' in data:
            data['time'] = data['asctime']
            del data['asctime']
        if 'levelname' in data:
            data['level'] = data['levelname'].lower()
            del data['levelname']

        return json.dumps(data, cls=self.encoder)
