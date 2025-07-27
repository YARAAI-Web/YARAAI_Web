rule auto_rule_20250727044738_4583 {
  strings:
    $o0 = "x18000003C" wide ascii nocase
  condition:
    all of them
}