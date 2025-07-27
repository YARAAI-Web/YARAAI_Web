rule auto_rule_20250726203620_0206 {
  strings:
    $o0 = "x23CA00000000LL" wide ascii nocase
  condition:
    all of them
}