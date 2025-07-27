rule auto_rule_20250726141009_8780 {
  strings:
    $o0 = "dwExStyle" wide ascii nocase
    $o1 = "a4444_1" wide ascii nocase
  condition:
    all of them
}