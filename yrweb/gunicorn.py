"""Gunicorn WSGI server configuration."""
from multiprocessing import cpu_count


def count_workers():
    return (2*cpu_count())+1


bind = '0.0.0.0:8000'
workers = count_workers()
timeout = 3000
