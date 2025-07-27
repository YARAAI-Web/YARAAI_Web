rule auto_rule_20250726065913_3728 {
  strings:
    $o0 = "word_1E7A2" wide ascii nocase
    $o1 = "dword_78258" wide ascii nocase
  condition:
    all of them
}