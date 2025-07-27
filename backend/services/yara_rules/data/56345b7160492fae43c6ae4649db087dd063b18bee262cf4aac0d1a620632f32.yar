rule auto_rule_20250726180336_0414 {
  strings:
    $o0 = "uiAction" wide ascii nocase
    $o1 = "dwExStyle" wide ascii nocase
    $o2 = "lpDialogFunc" wide ascii nocase
    $o3 = "FindWindowA" wide ascii nocase
  condition:
    4 of ($o*)
}