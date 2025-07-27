rule auto_rule_20250726060125_3811 {
  strings:
    $o0 = "acmStreamReset" wide ascii nocase
    $o1 = "fccType" wide ascii nocase
  condition:
    all of them
}