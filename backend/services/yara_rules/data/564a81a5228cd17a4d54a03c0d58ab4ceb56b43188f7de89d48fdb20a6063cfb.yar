rule auto_rule_20250726061247_3593 {
  strings:
    $o0 = "DriverEntry" wide ascii nocase
    $o1 = "word_1EA26" wide ascii nocase
  condition:
    all of them
}