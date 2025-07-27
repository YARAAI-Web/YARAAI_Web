rule auto_rule_20250726194133_6866 {
  strings:
    $o0 = "GetCursorInfo" wide ascii nocase
    $o1 = "dwVer" wide ascii nocase
    $o2 = "GetUserObjectSecurity" wide ascii nocase
    $o3 = "hWndChild" wide ascii nocase
    $o4 = "IMPSetIMEA" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726194137_6099 {
  strings:
    $o0 = "pDevmode" wide ascii nocase
    $o1 = "lResult" wide ascii nocase
    $o2 = "FreeDDElParam" wide ascii nocase
    $o3 = "uiAction" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726194140_1964 {
  condition:
    auto_rule_20250726194133_6866 or auto_rule_20250726194137_6099
}