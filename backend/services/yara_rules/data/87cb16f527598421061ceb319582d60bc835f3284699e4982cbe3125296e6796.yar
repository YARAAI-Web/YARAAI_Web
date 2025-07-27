rule auto_rule_20250726171505_3304 {
  strings:
    $o0 = "dword_450000" wide ascii nocase
  condition:
    all of them
}