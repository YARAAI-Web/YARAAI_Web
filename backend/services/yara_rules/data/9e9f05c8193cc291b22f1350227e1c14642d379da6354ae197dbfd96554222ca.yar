rule auto_rule_20250726064053_4915 {
  strings:
    $o0 = "dword_402FA8" wide ascii nocase
  condition:
    all of them
}