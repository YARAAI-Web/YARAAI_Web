rule auto_rule_20250726143006_1463 {
  strings:
    $o0 = "HiliteMenuItem" wide ascii nocase
    $o1 = "DefineDosDeviceA" wide ascii nocase
    $o2 = "LocalFlags" wide ascii nocase
    $o3 = "DdeDisconnect" wide ascii nocase
  condition:
    4 of ($o*)
}