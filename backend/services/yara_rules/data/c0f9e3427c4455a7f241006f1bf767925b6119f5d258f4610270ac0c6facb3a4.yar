rule auto_rule_20250726230101_3992 {
  strings:
    $o0 = "dword_1400C7744" wide ascii nocase
    $o1 = "dword_1400C73E0" wide ascii nocase
  condition:
    all of them
}