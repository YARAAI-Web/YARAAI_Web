rule auto_rule_20250727032550_6853 {
  strings:
    $o0 = "x17000u" wide ascii nocase
  condition:
    all of them
}