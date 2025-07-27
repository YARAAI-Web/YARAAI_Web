rule auto_rule_20250726063844_1188 {
  strings:
    $o0 = "x4D0BE9" wide ascii nocase
    $o1 = "x191" wide ascii nocase
  condition:
    all of them
}