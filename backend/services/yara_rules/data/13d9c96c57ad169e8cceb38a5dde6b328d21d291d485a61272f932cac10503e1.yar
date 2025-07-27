rule auto_rule_20250726130806_7193 {
  strings:
    $o0 = "aGggstgggggcgcr" wide ascii nocase
    $o1 = "dword_405D48" wide ascii nocase
  condition:
    all of them
}