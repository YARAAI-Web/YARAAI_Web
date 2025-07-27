rule auto_rule_20250726213923_3438 {
  strings:
    $o0 = "dword_4D30D0" wide ascii nocase
  condition:
    all of them
}