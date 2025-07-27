rule auto_rule_20250726234436_4728 {
  strings:
    $o0 = "dword_1400C7534" wide ascii nocase
    $o1 = "dword_1400C74F8" wide ascii nocase
  condition:
    all of them
}