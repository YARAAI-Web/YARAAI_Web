rule auto_rule_20250726162011_9372 {
  strings:
    $o0 = "dword_46D148" wide ascii nocase
  condition:
    all of them
}