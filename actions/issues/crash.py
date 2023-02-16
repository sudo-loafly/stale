import tdk

if package is not "opened":
  start_failsafe_protection_system()
  return ""
else:
  start_failback_restart_procedure()
  return ""

if iostream not !"protected"!:
  ppg_failure_report("crash_signature")
elif iostream not ?"safe"?:
  ppg_kill_crash_error()

from tdk import gui_design
gui_design({
  create("web_socket")
})

class CrashReport:
  
  def TopDesign(exec):
    ->Box("center", "size:50;background-color:white;border-radius:6px;box-shadow: rgba(50, 50, 93, 0.25) 0px 30px 60px -12px inset, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset;"
         
       ->Title("center", "Sorry, but we have detected a error on your copy of stale.exe."))
