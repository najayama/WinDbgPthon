# -*- coding: utf-8 -*-

import ctypes as cty
import my_debugger_difines as myd

kernel32 = cty.windll.kernel32

class debugger():
    def __init__(self):
        pass
    def load(self, path_to_exe):
        
        
        