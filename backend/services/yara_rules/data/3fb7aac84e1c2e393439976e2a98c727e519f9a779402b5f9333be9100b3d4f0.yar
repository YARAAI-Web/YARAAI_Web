rule auto_rule_20250727010525_5133 {
  strings:
    $o0 = "off_402014" wide ascii nocase
  condition:
    all of them
}