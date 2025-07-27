rule auto_rule_20250727031141_1644 {
  strings:
    $o0 = "dword_77EF0" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}