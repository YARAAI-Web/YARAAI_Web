rule auto_rule_20250726115256_2662 {
  strings:
    $o0 = "x79AB00000000LL" wide ascii nocase
  condition:
    all of them
}