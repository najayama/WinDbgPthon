import naja_debugger

debugger = naja_debugger.debugger()

#debugger.make_debuggee_process(b"C:\\WINDOWS\\system32\\calc.exe")


string_pid = input("Enter PID of process: ")
int_pid = int(string_pid)
debugger.attach_process(int_pid)

