rule auto_rule_20250726103916_0461 {
  strings:
    $o0 = "DefDlgProcW" wide ascii nocase
    $o1 = "uSizeStruct" wide ascii nocase
    $o2 = "WINNLSEnableIME" wide ascii nocase
    $o3 = "DdeNameService" wide ascii nocase
    $o4 = "grfFlags" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726103919_5221 {
  strings:
    $o0 = "OpenWindowStationA" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726103923_9577 {
  condition:
    auto_rule_20250726103916_0461 or auto_rule_20250726103919_5221
}