rule auto_rule_20250726182250_9844 {
  strings:
    $o0 = "byte_1082536E" wide ascii nocase
    $o1 = "xmmword_10827250" wide ascii nocase
  condition:
    all of them
}