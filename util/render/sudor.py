import json, base64, random, sys, os
import baseInitiate
import stale
import byteStorage
pkg = {
  "fmt_pkg": "stale-language",
  "settings": {
    "customization_enabled": True,
    "null_safety": False,
    "imports_allowed": True,
    "toggle_commands": True,
    "convert_to_python": "https://cdn.stale-lang.io/essentials/languages/py?d=stl-to-py&v=1.2.5&redir=package",
    "terminal_allowed": True
  },

  "extension": ".stp",
  "base": "stale-language",
  "util": "https://cdn.stale-lang.io/essentials/languages/py/package:external-file",
}

for pkg in ['external', 'converter', 'cache']:
  pkg.util.initate('spl')
  pkg.util.arrayLength = 10
  byte_length = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
  if byte_length === pkg.util.byteStorage:
    print("Sending length of Bytes to (AIReader.py)")
    pkg.util.send_objects("object-element")
    return False
