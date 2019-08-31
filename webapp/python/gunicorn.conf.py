#import multiprocessing

bind = 'unix:/var/run/torb/gunicorn.sock'
backlog = 2048

workers = 1
#workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
threads = 1
#threads = 1500
worker_connections = 1000
#worker_connections = 1500
timeout = 30
keepalive = 2

daemon = False
raw_env = [
    # 'DJANGO_SECRET_KEY=something',
    # 'SPAM=eggs',
]
pidfile = '/tmp/gunicorn.pid'
umask = 0
user = None
group = None
tmp_upload_dir = None

#
#   Logging
#
#   logfile - The path to a log file to write to.
#
#       A path string. "-" means log to stdout.
#
#   loglevel - The granularity of log output
#
#       A string of "debug", "info", "warning", "error", "critical"
#

errorlog = '/tmp/gunicorn.error.log'
#errorlog = None
loglevel = 'info'
accesslog = '/tmp/gunicorn.access.log'
#accesslog = None
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
