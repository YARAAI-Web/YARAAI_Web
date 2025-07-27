rule auto_rule_20250727005615_2384 {
  strings:
    $o0 = "x5DD361" wide ascii nocase
  condition:
    all of them
}