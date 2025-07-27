rule auto_rule_20250726134704_1735 {
  strings:
    $o0 = "SetBitmapDimensionEx" wide ascii nocase
    $o1 = "x23A3" wide ascii nocase
  condition:
    all of them
}