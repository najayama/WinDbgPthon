# -*- coding: utf-8 -*-

import ctypes
import constants_and_structure as mydef

kernel32 = ctypes.windll.kernel32

class debugger():
    def __init__(self):
        self.process_handle = None
        self.pid = None
        self.debugger_active = False
    
    def print_error(self):
        print("[*] Error: 0x%08x." % kernel32.GetLastError())
        print("See https://msdn.microsoft.com/", end="")
        print("en-us/library/cc231199.aspx for more detail.")
    
    def make_debuggee_process(self, path_to_exe):
        
        #constants for dwcreationflags
        #creation_flags = mydef.CREATE_NEW_CONSOLE
        creation_flags = mydef.DEBUG_PROCESS
        
        #make and init stracture to call CreateProcessA
        startupinfo = mydef.STARTUPINFO()
        processinformation = mydef.PROCESS_INFORMATION()
        
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
            self.pid = processinformation.dwProcessId
            return None
        else:
            self.print_error()
            return None
        
    def wrapper_OpenProcess(self, pid):
        _process_handle = kernel32.OpenProcess(mydef.PROCESS_ALL_ACCESS, False, pid)
        return _process_handle
    
    def attach_process(self, pid):
        
        self.process_handle = self.wrapper_OpenProcess(pid)
        
        #try attach and return if fail to.
        if kernel32.DebugActiveProcess(pid):
            #save  status of debugger
            self.debugger_active = True
            self.pid = int(pid)
        else:
            self.print_error()
     
    #def wait_debug_event(self):
    #This shoud be called after attach_to_process or make_debuggee_process.    
        
     #   debug_event = mydef.DEBUG_EVENT()
        
        
        