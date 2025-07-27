rule auto_rule_20250726095504_5482 {
  strings:
    $o0 = "x7B4D" wide ascii nocase
  condition:
    all of them
}