rule auto_rule_20250726091705_5761 {
  strings:
    $o0 = "private" wide ascii nocase
    $o1 = "x401C6B" wide ascii nocase
  condition:
    all of them
}