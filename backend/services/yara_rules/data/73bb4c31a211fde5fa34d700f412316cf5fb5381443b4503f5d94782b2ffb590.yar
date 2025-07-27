rule auto_rule_20250726155402_1283 {
  strings:
    $o0 = "dword_41D974" wide ascii nocase
  condition:
    all of them
}