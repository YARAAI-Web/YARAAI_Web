rule auto_rule_20250726124836_6525 {
  strings:
    $o0 = "dword_4022A8" wide ascii nocase
  condition:
    all of them
}