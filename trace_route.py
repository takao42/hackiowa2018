from utilities import to_int
from sarge import capture_stdout
import time


def async_parse_tracert(target, on_new_node):
    p = capture_stdout('tracert {}'.format(target), async_=True)
    num_timeouts = 0

    while p.returncodes[0] is None:
        line = p.stdout.readline()
        line = line.decode('utf-8')
        elems = line.split()
        elems = [value for value in elems if value != 'ms']
        if (len(elems) == 5 or len(elems) == 6) and elems[0].isdigit():
            new_node = {
                'delays': (to_int(elems[1]), to_int(elems[2]), to_int(elems[3]))
            }
            if len(elems) == 6:
                new_node['name'] = elems[4]
                new_node['addr'] = elems[5].strip('[').strip(']')
            else:
                new_node['addr'] = elems[4]
            on_new_node(new_node)
            num_timeouts = 0
        elif len(elems) > 0 and elems[-1] == 'out.':
            num_timeouts += 1
            # on_new_node(None)
            if num_timeouts >= 1:
                return -1
        p.commands[0].poll()
        time.sleep(0.05)

    return p.returncodes[0]
