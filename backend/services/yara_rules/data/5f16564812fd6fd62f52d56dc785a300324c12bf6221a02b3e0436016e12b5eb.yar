rule auto_rule_20250726164514_7908 {
  strings:
    $o0 = "byte_4C12A9" wide ascii nocase
    $o1 = "liDistanceToMove" wide ascii nocase
  condition:
    all of them
}