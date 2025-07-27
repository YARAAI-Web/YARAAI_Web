rule auto_rule_20250726224346_5257 {
  strings:
    $o0 = "lParam2" wide ascii nocase
  condition:
    all of them
}