import multiprocessing

bind = '127.0.0.1:9997'
workers = multiprocessing.cpu_count() * 2 + 1
daemon = True
pidfile = 'gunicorn.pid'
logfile = 'gunicorn.log'
preload_app = True

# Minizing impact of any potential memory leaks
max_requests = 1000
