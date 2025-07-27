rule auto_rule_20250726212222_1352 {
  strings:
    $o0 = "dword_4D30BC" wide ascii nocase
  condition:
    all of them
}