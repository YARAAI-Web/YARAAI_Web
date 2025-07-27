rule auto_rule_20250726093822_1234 {
  strings:
    $o0 = "dword_45CAC4" wide ascii nocase
  condition:
    all of them
}