import platform
from ctypes import *

if platform.system() == 'Windows':
    libc = cdll.LoadLibrary('msvcrt.dll')
elif platform.system() =='Linux':
    libc = cdll.LoadLibrary('libc.so.6')
    
libc.printf('Lello ctypes!\n')
libc.printf('Lello ctypes!\n')
libc.printf('Lello ctypes!\n')
libc.printf('Lello ctypes!\n')

libc.printf('%s\n', 'here!')        # here!
libc.printf('%S\n', u'there!')      # there!
libc.printf('%d\n', 42)             # 42
libc.printf('%ld\n', 60000000)      # 60000000

#libc.printf('%f\n', 3.14)          #>>> ctypes.ArgumentError
#libc.printf('%f\n', c_float(3.14)) #>>> dont know why 0.000000
libc.printf('%f\n', c_double(3.14)) # 3.140000
