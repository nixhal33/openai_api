import os
import threading
import time

from crud import filesystem
from process import procmg
from pyos import pyos

if __name__=="__main__":
    file_system=filesystem()
    procmg=procmg()
    os_sim=pyos(filesystem,procmg)
    os_sim.shell()




