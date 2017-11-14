'''
@author: naja yama
'''

import ctypes

#rename types name like microsoft
WORD    = ctypes.c_ushort
DWORD   = ctypes.c_ulong
LPBYTE  = ctypes.POINTER(ctypes.c_ubyte)
LPTSTR  = ctypes.POINTER(ctypes.c_char)
HANDLE  = ctypes.c_void_p


#constants
DEBUG_PROCESS      = 0x00000001
CREATE_NEW_CONSOLE = 0x00000010

#structure for createprocessA()
class STARTUPINFO(ctypes.Structure):
    _fields_ = [
        ("cb",            DWORD),        
        ("lpReserved",    LPTSTR), 
        ("lpDesktop",     LPTSTR),  
        ("lpTitle",       LPTSTR),
        ("dwX",           DWORD),
        ("dwY",           DWORD),
        ("dwXSize",       DWORD),
        ("dwYSize",       DWORD),
        ("dwXCountChars", DWORD),
        ("dwYCountChars", DWORD),
        ("dwFillAttribute",DWORD),
        ("dwFlags",       DWORD),
        ("wShowWindow",   WORD),
        ("cbReserved2",   WORD),
        ("lpReserved2",   LPBYTE),
        ("hStdInput",     HANDLE),
        ("hStdOutput",    HANDLE),
        ("hStdError",     HANDLE),
        ]


class PROCESSINFORMATION(ctypes.Structure):
    _fields_ = [
        ("hProcess",    HANDLE),
        ("hThread",     HANDLE),
        ("dwProcessId", DWORD),
        ("dwThreadId",  DWORD),
        ]
    
