from .tree import sitemap_tree_for_homepage as sitemap_tree_internal

import sys
import threading
import _thread as thread


def quit_function(fn_name):
    sys.stderr.flush()
    thread.interrupt_main()


def exit_after(s):
    '''
    use as decorator to exit process if 
    function takes longer than s seconds
    '''
    def outer(fn):
        def inner(*args, **kwargs):
            timer = threading.Timer(s, quit_function, args=[fn.__name__])
            timer.start()
            try:
                result = fn(*args, **kwargs)
            finally:
                timer.cancel()
            return result
        return inner
    return outer

def sitemap_tree_for_homepage(*args, **kwargs):

    return_data = None

    timeout = kwargs.get("timeout")

    if timeout:
        try:
            time_kill_sitemap_tree = exit_after(timeout)(sitemap_tree_internal)
            return_data = time_kill_sitemap_tree(*args)
        except KeyboardInterrupt:
            pass
    else:
        return_data = sitemap_tree_internal(*args)

    return return_data
