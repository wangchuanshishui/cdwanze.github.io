<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 获取项目DSN地址</a></li>
<li><a href="#orgheadline2">2. 和flask整合</a></li>
<li><a href="#orgheadline3">3. 和logging模块整合</a></li>
</ul>
</div>
</nav>


# 获取项目DSN地址<a id="orgheadline1"></a>

在Sentry服务器上创建项目，然后获取DSN地址。

# 和flask整合<a id="orgheadline2"></a>

flask整合如下所示:

    pip install raven[flask]

    from raven.contrib.flask import Sentry
    sentry = Sentry(app, dsn='https://<key>:<secret>@app.getsentry.com/<project>')

如果这里没有指定dsn值，则会自动在flask的settings里面读取 `SENTRY_DSN` 的值。

# 和logging模块整合<a id="orgheadline3"></a>

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            },
        'sentry': {
            'level': 'INFO',
            'class': 'raven.handlers.logging.SentryHandler',
            'dsn': SENTRY_DSN,
            },
        },

    'loggers': {
        '': {
            'handlers': ['console', 'sentry'],
            'level': 'INFO',
            'propagate': False,
            },
    }
}

# 在应用初始化的地方
import logging
import logging.config
logging.config.dictConfig(LOGGING)
```