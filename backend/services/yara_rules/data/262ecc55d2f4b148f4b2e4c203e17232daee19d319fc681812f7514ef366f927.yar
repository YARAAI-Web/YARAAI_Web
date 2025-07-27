rule auto_rule_20250726091331_7267 {
  strings:
    $o0 = "_cropzeros_l" wide ascii nocase
    $o1 = "off_4BAD98" wide ascii nocase
  condition:
    all of them
}