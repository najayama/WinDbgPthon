# -*- coding: utf-8 -*-

import ctypes as cty
import n_debugger_difines as ndef

kernel32 = cty.windll.kernel32

class debugger():
    def __init__(self):
        pass
    
    def load(self, path_to_exe):
        
        #dwcreationflagsのための定数
        #creation_flags = ndef.CREATE_NEW_CONSOLE
        creation_flags = ndef.DEBUG_PROCESS
        
        #各構造体をインスタンス化
        startupinfo = ndef.STARTUPINFO()
        process_information = ndef.PROCESS_INFORMATION()
        
        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x0
        
        startupinfo.cb = cty.sizeof(startupinfo)
        
        if kernel32.CreateProcessA(path_to_exe,
                                   None,
                                   None,
                                   None,
                                   None,
                                   creation_flags,
                                   None,
                                   None,
                                   cty.byref(startupinfo),
                                   cty.byref(process_information)):
            print("success")
            return 0
        else:
            print("[*] Error: 0x%08x." % kernel32.GetLastError())
            return None
        

            
                                   
                                   
        
        