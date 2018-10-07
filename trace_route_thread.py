import threading
from uuid import uuid4
from trace_route_db import *
from trace_route import async_parse_tracert


threads = []


def worker(task_id, target):
    """thread worker function
    """

    insert_task(task_id, target)
    insert_new_result(task_id)

    """ Run tracert """

    def on_new_node(new_node):
        append_result(task_id, new_node)

    return_code = async_parse_tracert(target, on_new_node)

    if return_code == -1:
        update_result_status(task_id, 'timeout')
    elif return_code == 0:
        update_result_status(task_id, 'success')
    else:
        update_result_status(task_id, 'error')


def start_task(target):
    task_id = str(uuid4())
    t = threading.Thread(target=worker, args=(task_id, target,))
    threads.append(t)
    t.start()
    return task_id
