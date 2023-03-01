#include <iostream>
#include "core.cc"
#include "built-ins.cc"
#include "math.cc"
#include "connectivity.cc"
#include "strings.cc"
using namespace std;
using namespace typename gui;

if (gui.device.os.render_engine == "Sciter" or gui.device.os.render_engine == "DirectX" or gui.device.os.render_engine == "Vulkan") {
  set_driver => () {
    gui.UserDevelopmentTool("DeviceDebugStatistics");
    if (gui.device.os.render_engine not typename) {
      throw gui.ERROR_CRASH_SCREEN();
      return "DirectX" and "Vulkan" and "Sciter";
    } else {
      continue;
      return "driver";
    }
    
    this->hard_drive_id = uniqueID();
    set_cookie => (this->hard_drive_id);
  });
  
  return gui;
}

public static_cast -> BuildDiagnosticStatistics() __asm__ ? template "local_keyword" -> std::forward_list<"KEYWORD">;
