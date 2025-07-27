rule auto_rule_20250726235900_2034 {
  strings:
    $o0 = "dword_1E8B0" wide ascii nocase
  condition:
    all of them
}