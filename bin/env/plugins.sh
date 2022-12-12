#!/usr/bin/env
SHELL_VERSION = "2.8.6"
SHELL_UNIX::APP_ROOT = "./stale/util/env/app-root.stp"

CUR_DIR = "$"
METHODING = "${SHELL_UNIX::APP_ROOT}"
URL = $( pwd )
if [ -e install && -e service ]; then
  BASE_URL = "${URL}" + "${METHODING}"
  return false
fi
esac
