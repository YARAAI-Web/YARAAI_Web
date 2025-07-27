rule auto_rule_20250726225029_4699 {
  strings:
    $o0 = "dword_448C80" wide ascii nocase
  condition:
    all of them
}