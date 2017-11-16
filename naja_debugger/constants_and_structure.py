###### I referenced Gray Hay python (by Justin seitz ,No Starch Pr,
###### ISBN:978-1593271923)

'''
@author: najayama
'''

import ctypes

#rename types name like microsoft
WORD = ctypes.c_ushort
DWORD = ctypes.c_ulong
LPBYTE = ctypes.POINTER(ctypes.c_ubyte)
LPTSTR = ctypes.POINTER(ctypes.c_char)
HANDLE = ctypes.c_void_p
PVOID = ctypes.c_void_p
UINT_PTR = ctypes.c_ulong


#constants
DEBUG_PROCESS = 0x00000001
CREATE_NEW_CONSOLE = 0x00000010
INFINITE = -1
PROCESS_ALL_ACCESS = 0x001F0FFF

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


class PROCESS_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("hProcess",    HANDLE),
        ("hThread",     HANDLE),
        ("dwProcessId", DWORD),
        ("dwThreadId",  DWORD),
    ]

class EXCEPTION_RECORD(ctypes.Structure):
    pass


EXCEPTION_RECORD._fields_ = [
        ("ExceptionCode",        DWORD),
        ("ExceptionFlags",       DWORD),
        ("ExceptionRecord",      ctypes.POINTER(EXCEPTION_RECORD)),
        ("ExceptionAddress",     PVOID),
        ("NumberParameters",     DWORD),
        ("ExceptionInformation", UINT_PTR * 15),
    ]

    
    
    
    
    
class EXCEPTION_DEBUG_INFO(ctypes.Structure):
    _fields_ = [
        ("ExceptionRecord",    EXCEPTION_RECORD),
        ("dwFirstChance",      DWORD),
        ]    
    
class _DEBUG_EVENT_UNION():
    _fields_ = [
        ("Exception",         EXCEPTION_DEBUG_INFO)
##IF you need, add below.
#        ("CreateThread",
#        ("CreateProcessInfo",
#        ("ExitThread",
#        ("ExitProcess",
#        ("LoadDll",
#        ("UnloadDll",
#        ("DebugString",    
#        ("RipInfo",
    ]
        

class DEBUG_EVENT():
    _fields_ = [
        ("dwDebugEventCode", DWORD),
        ("dwProcessId",      DWORD),
        ("dwThreadId",       DWORD),
        ("u",                _DEBUG_EVENT_UNION)
    ]
    
