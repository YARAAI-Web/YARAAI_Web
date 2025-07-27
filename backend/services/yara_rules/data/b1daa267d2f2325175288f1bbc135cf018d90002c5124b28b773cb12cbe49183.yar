rule auto_rule_20250726212841_3825 {
  strings:
    $o0 = "dword_1400914A0" wide ascii nocase
  condition:
    all of them
}