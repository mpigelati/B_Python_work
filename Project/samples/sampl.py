import subprocess
import os

from pyand import ADB

from pyand import ADB, Fastboot
adb = ADB()
adb.get_devices()