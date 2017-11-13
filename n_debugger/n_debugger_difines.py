# -*- coding: utf-8 -*-
'''
@author: naja yama
'''

import ctypes as cty


WORD    = cty.c_ushort
DWORD   = cty.c_ulong
LPBYTE  = cty.POINTER(cty.c_ubyte)
LPTSTR  = cty.POINTER(cty.c_char)
HANDLE  = cty.c_void_p


#定数
DEBUG_PROCESS      = 0x00000001
CREATE_NEW_CONSOLE = 0x00000010

#関数CreateprocessA()のための構造体
class STARTUPINFO(cty.Structure):
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


class PROCESS_INFORMATION(cty.Structure):
    _fields_ = [
        ("hProcess",    HANDLE),
        ("hThread",     HANDLE),
        ("dwProcessId", DWORD),
        ("dwThreadId",  DWORD),
        ]
    
