#include "tdkc.cc"

connect_status("false");

STATUS => {
  false-equation: "false",
  data_: "true"
}

if (true) {
  kill_network_status_problem.st(data_);
  return { CON.CC_NETWORK };
}
