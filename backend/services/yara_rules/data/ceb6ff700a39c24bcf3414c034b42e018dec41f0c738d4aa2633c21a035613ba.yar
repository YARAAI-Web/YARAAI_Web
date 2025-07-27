rule auto_rule_20250726193020_9464 {
  strings:
    $o0 = "byte_640331CB" wide ascii nocase
  condition:
    all of them
}