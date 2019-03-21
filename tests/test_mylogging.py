import sys
import unittest
from datetime import datetime
from io import StringIO

import mylogging


class MyloggingTest(unittest.TestCase):
    def setUp(self):
        self.stderr = StringIO()
        sys.stderr = self.stderr

    def tearDown(self):
        sys.stderr = sys.__stderr__

    def test_getLogger_text(self):
        logger = mylogging.getLogger('test_getLogger_text', fmt='text')
        logger.info('This is text test.')

        log = self.stderr.getvalue()
        datetime.strptime(log[0:25], '%Y-%m-%dT%H:%M:%S+09:00')
        self.assertEqual(' [INFO] This is text test.\n', log[25:])

    def test_getLogger_json(self):
        logger = mylogging.getLogger('test_getLogger_json', fmt='json')
        logger.info('This is json test.')

        import json
        log = json.loads(self.stderr.getvalue())
        datetime.strptime(log['time'], '%Y-%m-%dT%H:%M:%S+09:00')
        del log['time']
        expect = {'level': 'info',
                  'message': 'This is json test.',
                  'name': 'test_getLogger_json'}
        self.assertDictEqual(log, expect)
