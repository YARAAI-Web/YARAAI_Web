rule auto_rule_20250726220002_7404 {
  strings:
    $o0 = "GetUserObjectInformationW" wide ascii nocase
    $o1 = "uiAction" wide ascii nocase
    $o2 = "pDevmode" wide ascii nocase
    $o3 = "cmdInsert" wide ascii nocase
    $o4 = "GetProcessDefaultLayout" wide ascii nocase
  condition:
    4 of ($o*)
}