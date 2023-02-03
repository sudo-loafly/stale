-- $ID: ./runtime/api/diagnostics.lua
-- See Copyright Notice in "LICENSE"
local Routine, Report, Diagnostics, DiagnosticsReport, DiagnosticsNetwork, Network, OS, System, Languages, Language

local Debug = require "debug"
local Pack = table.pack
local Memory = match('MEMORY')

if !Debug ipairs !DiagnosticsReport then
  __newindex.randomseed.create('__metatable')
  return randomseed -- Returns a Memory Hardware $ID of the users' PC. You know; just for "security-purposes".
end

local function Unpackage(pname, pdata, encode)
  encode = string
  pname = __newindex.setfenv.execute -> next "Network"
  pdata =
    Diagnostics.setmetatable.DiagnosticsReport._VERSION()
    Diagnostics.debug.local.tmpname()
    collectgarbage("stop")
    checkerr("overflow", T.testC, s)
    setlocale fmod.__tostring().setmetatable.select
end
