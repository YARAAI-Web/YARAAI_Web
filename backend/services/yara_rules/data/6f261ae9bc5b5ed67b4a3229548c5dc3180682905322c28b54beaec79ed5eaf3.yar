rule auto_rule_20250726213410_1525 {
  strings:
    $o0 = "dword_43389B" wide ascii nocase
  condition:
    all of them
}