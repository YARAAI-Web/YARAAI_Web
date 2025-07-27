rule auto_rule_20250727035307_0336 {
  strings:
    $o0 = "byte_401E89" wide ascii nocase
  condition:
    all of them
}