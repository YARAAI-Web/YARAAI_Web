rule auto_rule_20250726093144_4938 {
  strings:
    $o0 = "dword_4657D0" wide ascii nocase
  condition:
    all of them
}