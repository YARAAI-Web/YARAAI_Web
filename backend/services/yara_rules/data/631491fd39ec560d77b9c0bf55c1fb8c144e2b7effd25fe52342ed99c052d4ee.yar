rule auto_rule_20250726165009_2971 {
  strings:
    $o0 = "aExternalerror" wide ascii nocase
    $o1 = "vpermq" wide ascii nocase
  condition:
    all of them
}