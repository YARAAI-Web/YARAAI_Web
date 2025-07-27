rule auto_rule_20250726084114_2024 {
  strings:
    $o0 = "dword_781DC" wide ascii nocase
  condition:
    all of them
}