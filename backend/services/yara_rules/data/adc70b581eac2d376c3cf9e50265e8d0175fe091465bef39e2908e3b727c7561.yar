rule auto_rule_20250726134749_0172 {
  strings:
    $o0 = "dword_78320" wide ascii nocase
  condition:
    all of them
}