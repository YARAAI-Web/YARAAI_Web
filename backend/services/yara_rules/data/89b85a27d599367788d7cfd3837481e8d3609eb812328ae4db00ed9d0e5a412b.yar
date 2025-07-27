rule auto_rule_20250726232259_7272 {
  strings:
    $o0 = "dword_6502FD90" wide ascii nocase
    $o1 = "F58h" wide ascii nocase
  condition:
    all of them
}