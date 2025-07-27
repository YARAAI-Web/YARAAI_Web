rule auto_rule_20250726082232_1527 {
  strings:
    $o0 = "dword_4657D0" wide ascii nocase
  condition:
    all of them
}