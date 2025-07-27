rule auto_rule_20250726214146_6731 {
  strings:
    $o0 = "dxDst" wide ascii nocase
  condition:
    all of them
}