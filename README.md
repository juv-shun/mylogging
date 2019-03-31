## mylogging

This is Python logger for myself.

```sh
pip install git+https://github.com/juv-shun/mylogging
```

## How to use

```python
import mylogging

logger = mylogging.getLogger('sample', fmt='json')
logger.info('This is log.')
# {"message": "This is log.", "name": "sample", "time": "2019-03-21T16:02:12+09:00", "level": "info"}
```
