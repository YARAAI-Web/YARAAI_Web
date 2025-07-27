rule auto_rule_20250726074730_1874 {
  strings:
    $o0 = "dword_77FC0" wide ascii nocase
  condition:
    all of them
}