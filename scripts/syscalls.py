import sim, syscall_strings, sys

if sys.maxsize == 2**31-1:
  __syscall_strings = syscall_strings.syscall_strings_32
else:
  __syscall_strings = syscall_strings.syscall_strings_64

def syscall_name(syscall_number):
  return '%s[%d]' % (__syscall_strings.get(syscall_number, 'unknown'), syscall_number)

class LogSyscalls:
  def hook_syscall_enter(self, threadid, coreid, time, syscall_number, args):
    print '[SYSCALL] @%10d ns: %-27s thread(%3d) core(%3d) args%s' % (time/1e6, syscall_name(syscall_number), threadid, coreid, args)

  def hook_syscall_exit(self, threadid, coreid, time, ret_val, emulated):
    print '[SYSCALL] @%10d ns:                        exit thread(%3d) core(%3d) ret_val(%d) emulated(%s)' % (time/1e6, threadid, coreid, ret_val, emulated)

sim.util.register(LogSyscalls())
