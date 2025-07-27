rule auto_rule_20250726164535_6113 {
  strings:
    $o0 = "dword_78134" wide ascii nocase
  condition:
    all of them
}