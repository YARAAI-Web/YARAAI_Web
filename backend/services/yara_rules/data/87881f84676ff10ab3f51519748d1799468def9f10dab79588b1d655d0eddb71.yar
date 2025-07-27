rule auto_rule_20250727020140_3510 {
  strings:
    $o0 = "byte_4186F3" wide ascii nocase
  condition:
    all of them
}