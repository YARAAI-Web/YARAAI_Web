rule auto_rule_20250726120827_2948 {
  strings:
    $o0 = "dword_42EEB8" wide ascii nocase
    $o1 = "dword_42EED4" wide ascii nocase
  condition:
    all of them
}