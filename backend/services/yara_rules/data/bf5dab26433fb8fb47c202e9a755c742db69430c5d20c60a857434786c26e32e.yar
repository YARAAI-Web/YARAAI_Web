rule auto_rule_20250726123950_9156 {
  strings:
    $o0 = "hwndCombo" wide ascii nocase
    $o1 = "dwExStyle" wide ascii nocase
    $o2 = "uMsg" wide ascii nocase
    $o3 = "hConvList" wide ascii nocase
  condition:
    4 of ($o*)
}