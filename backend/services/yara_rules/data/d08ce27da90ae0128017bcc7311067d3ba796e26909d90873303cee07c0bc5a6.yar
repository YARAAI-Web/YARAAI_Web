rule auto_rule_20250726175123_9614 {
  strings:
    $o0 = "lpCommProp" wide ascii nocase
    $o1 = "lpDeviceName" wide ascii nocase
    $o2 = "lpNewItem" wide ascii nocase
    $o3 = "lpKeyName" wide ascii nocase
    $o4 = "iMaxLength" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726175124_0448 {
  strings:
    $o0 = "wScanCode" wide ascii nocase
    $o1 = "CascadeWindows" wide ascii nocase
    $o2 = "UnregisterClassW" wide ascii nocase
    $o3 = "DdeNameService" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726175129_2697 {
  condition:
    auto_rule_20250726175123_9614 or auto_rule_20250726175124_0448
}