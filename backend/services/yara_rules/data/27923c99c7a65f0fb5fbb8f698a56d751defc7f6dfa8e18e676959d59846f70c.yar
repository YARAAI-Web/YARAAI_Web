rule auto_rule_20250726100322_5940 {
  strings:
    $o0 = "x2BDCu" wide ascii nocase
    $o1 = "x3FBBu" wide ascii nocase
  condition:
    all of them
}