rule auto_rule_20250726080922_1527 {
  strings:
    $o0 = "GetDoubleClickTime" wide ascii nocase
    $o1 = "SetWindowsHookA" wide ascii nocase
    $o2 = "lpsi" wide ascii nocase
    $o3 = "x17000u" wide ascii nocase
  condition:
    4 of ($o*)
}