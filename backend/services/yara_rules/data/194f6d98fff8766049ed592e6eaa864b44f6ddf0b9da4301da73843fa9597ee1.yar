rule auto_rule_20250726234748_3594 {
  strings:
    $o0 = "byte_42B5C4" wide ascii nocase
  condition:
    all of them
}