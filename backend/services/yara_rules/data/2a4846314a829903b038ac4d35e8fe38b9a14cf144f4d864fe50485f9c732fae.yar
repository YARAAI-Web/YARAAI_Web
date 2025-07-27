rule auto_rule_20250726101545_2254 {
  strings:
    $o0 = "stru_7845C" wide ascii nocase
  condition:
    all of them
}