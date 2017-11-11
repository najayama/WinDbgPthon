# -*- coding: utf-8 -*-

import ctypes as cty
import n_debugger_difines as ndbg

kernel32 = cty.windll.kernel32

class debugger():
    def __init__(self):
        pass
    def load(self, path_to_exe):
        
        #dwcreationflagsのための定数
        creation_flags = CREATE_NEW_CONSOLE
        #creation_flags = DEBUG_PROCESS
        
        #各構造体をインスタンス化
        startupinfo = ndbg.STARTUPINFO()
        process_information = PROCESS_INFOMATION()
        
        if kernel32.CreateProcessA(path_to_exe,
                                   None,
                                   None,
                                   None,
                                   None,
                                   creation_flags,
                                   None,
                                   None,
                                   startupinfo,
                                   process_information):
            print("success")
            return 0
        else:
            print("something wrong")
            return None
        

            
                                   
                                   
        
        