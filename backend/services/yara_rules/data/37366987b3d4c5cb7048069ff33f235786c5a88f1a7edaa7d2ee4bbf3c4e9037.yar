rule auto_rule_20250726083802_1612 {
  strings:
    $o0 = "byte_44E1C4" wide ascii nocase
  condition:
    all of them
}