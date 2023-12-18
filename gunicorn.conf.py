bind = '0.0.0.0:8000'  # Bind to the specified IP and port
workers = 4  # Number of worker processes
threads = 2  # Number of threads per worker
worker_class = 'gevent'  # Worker class for handling requests
worker_class = "uvicorn.workers.UvicornWorker"
timeout = 120  # Request timeout in seconds
keepalive = 5  # Interval for sending keep-alive messages to clients