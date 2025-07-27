rule auto_rule_20250726193450_6075 {
  strings:
    $o0 = "off_472080" wide ascii nocase
    $o1 = "dword_471A30" wide ascii nocase
  condition:
    all of them
}