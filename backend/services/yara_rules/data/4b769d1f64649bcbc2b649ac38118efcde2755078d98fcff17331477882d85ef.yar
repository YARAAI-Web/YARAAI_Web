rule auto_rule_20250726201124_0001 {
  strings:
    $o0 = "lpSearchFilter" wide ascii nocase
    $o1 = "dwBufferCoord" wide ascii nocase
    $o2 = "StrCmpNIW" wide ascii nocase
    $o3 = "lpwinsta" wide ascii nocase
    $o4 = "SHFileOperation" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726201127_8574 {
  strings:
    $o0 = "CreateWindowStationA" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726201131_6484 {
  condition:
    auto_rule_20250726201124_0001 or auto_rule_20250726201127_8574
}