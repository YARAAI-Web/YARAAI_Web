rule auto_rule_20250726145302_7303 {
  strings:
    $o0 = "FEE6h" wide ascii nocase
  condition:
    all of them
}