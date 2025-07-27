rule auto_rule_20250727020352_5548 {
  strings:
    $o0 = "x3EA8" wide ascii nocase
  condition:
    all of them
}