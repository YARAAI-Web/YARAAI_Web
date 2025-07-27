rule auto_rule_20250726185628_1930 {
  strings:
    $o0 = "x3873F" wide ascii nocase
  condition:
    all of them
}