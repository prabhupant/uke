import multiprocessing
from concurrent import futures


threads = multiprocessing.cpu_count()
thread_pool = futures.ThreadPoolExecutor(max_workers=threads)

callbacks = []
results = []


def run(f, *args, **kwargs):

    thread_pool._max_workers = threads
    thread_pool._adjust_thread_count()

    f = thread_pool.submit(f, *args, **kwargs)
    results.append(f)

    return f


def job(f):
    def run_job(*args, **kwargs):
        result = run(f, *args, **kwargs)

        for c in callbacks:
            result.add_done_callback(cb)

        return result

    return run_job


def callback(f):
    callbacks.append(f)

    def register_callback():
        f()

    return register_callback
