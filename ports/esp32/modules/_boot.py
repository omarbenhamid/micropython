import gc
import uos
from flashbdev import bdev

try:
    if bdev:
        uos.mount(bdev, '/')
except OSError:
    import inisetup
    vfs = inisetup.setup()

import machine
try:
    #LyraT requires to pull down IO13 for SDCARD to work ...
    machine.Pin(13, machine.Pin.OUT, machine.Pin.PULL_DOWN)
    uos.mount(machine.SDCard(), '/sdcard')
except OSError:
    print("Failed to mount SDCard")
    print(OSError)

gc.collect()
