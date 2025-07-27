rule auto_rule_20250727003746_1666 {
  strings:
    $o0 = "xC0000092" wide ascii nocase
    $o1 = "_byte_0" wide ascii nocase
  condition:
    all of them
}