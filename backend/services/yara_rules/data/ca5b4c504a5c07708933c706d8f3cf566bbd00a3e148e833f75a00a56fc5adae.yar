rule auto_rule_20250726062031_8201 {
  strings:
    $o0 = "dword_41A820" wide ascii nocase
  condition:
    all of them
}