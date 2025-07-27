rule auto_rule_20250727043225_1706 {
  strings:
    $o0 = "dword_1400E2498" wide ascii nocase
  condition:
    all of them
}