rule auto_rule_20250726120041_6642 {
  strings:
    $o0 = "EnumDisplayDevicesA" wide ascii nocase
    $o1 = "pData" wide ascii nocase
    $o2 = "GetClassInfoExA" wide ascii nocase
    $o3 = "StrToIntExA" wide ascii nocase
    $o4 = "GetProcessDefaultLayout" wide ascii nocase
  condition:
    4 of ($o*)
}