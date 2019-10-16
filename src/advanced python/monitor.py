from time import sleep
import os

print(os.getpid())
def set_proc_name(newname):
    from ctypes import cdll, byref, create_string_buffer
    libc = cdll.LoadLibrary('libc.so.6')
    buff = create_string_buffer(len(newname)+1)
    buff.value = newname
    libc.prctl(15, byref(buff), 0, 0, 0)

def get_proc_name():
    from ctypes import cdll, byref, create_string_buffer
    libc = cdll.LoadLibrary('libc.so.6')
    buff = create_string_buffer(128)
    # 16 == PR_GET_NAME from <linux/prctl.h>
    libc.prctl(16, byref(buff), 0, 0, 0)
    return buff.value

import sys
# sys.argv[0] == 'python'

# outputs 'python'
get_proc_name()

set_proc_name('pythontesting')

# outputs 'testing yeah'
get_proc_name()


def func(i):
    print(i)
    sleep(1)

for i in range(1, 100000000000000):
    func(i)