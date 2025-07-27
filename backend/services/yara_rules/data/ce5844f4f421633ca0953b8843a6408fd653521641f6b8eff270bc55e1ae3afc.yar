rule auto_rule_20250726231037_5885 {
  strings:
    $o0 = "dyDst" wide ascii nocase
  condition:
    all of them
}