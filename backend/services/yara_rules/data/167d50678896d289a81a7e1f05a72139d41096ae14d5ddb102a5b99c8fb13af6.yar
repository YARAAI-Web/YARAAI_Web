rule auto_rule_20250726210454_6145 {
  strings:
    $o0 = "byte_478B28" wide ascii nocase
  condition:
    all of them
}