rule auto_rule_20250726235111_5132 {
  strings:
    $o0 = "dword_402FB4" wide ascii nocase
  condition:
    all of them
}