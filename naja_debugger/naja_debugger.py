# -*- coding: utf-8 -*-

import ctypes
import constants_and_structure as mydef

kernel32 = ctypes.windll.kernel32

class debugger():
    def __init__(self):
        pass
    
    def print_error(self):
        print("[*] Error: 0x%08x." % kernel32.GetLastError())
        print("See https://msdn.microsoft.com/", end="")
        print("en-us/library/cc231199.aspx for more detail.")
    
    def make_debuggee_process(self, path_to_exe):
        
        #dwcreationflagsのための定数
        #creation_flags = mydef.CREATE_NEW_CONSOLE
        creation_flags = mydef.DEBUG_PROCESS
        
        #各構造体をインスタンス化し値を設定
        startupinfo = mydef.STARTUPINFO()
        processinformation = mydef.PROCESSINFORMATION()
        
        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x0
        startupinfo.cb = ctypes.sizeof(startupinfo)
        
        if kernel32.CreateProcessA(path_to_exe,
                                   None,
                                   None,
                                   None,
                                   None,
                                   creation_flags,
                                   None,
                                   None,
                                   ctypes.byref(startupinfo),
                                   ctypes.byref(processinformation)):
            print("Succusessfuly loanch the prsess!")
            print( "PID: %d" % (processinformation.dwProcessId))
            return None
        else:
            self.print_error()
            return None
        

        

            
                                   
                                   
        
        