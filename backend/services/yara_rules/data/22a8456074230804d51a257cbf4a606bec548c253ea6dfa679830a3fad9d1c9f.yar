rule auto_rule_20250726173817_1016 {
  strings:
    $o0 = "x2CE7u" wide ascii nocase
  condition:
    all of them
}