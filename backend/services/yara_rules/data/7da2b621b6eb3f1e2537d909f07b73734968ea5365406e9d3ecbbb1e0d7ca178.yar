rule auto_rule_20250726085819_6018 {
  strings:
    $o0 = "dword_469BA4" wide ascii nocase
    $o1 = "_ctype" wide ascii nocase
  condition:
    all of them
}