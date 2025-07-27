rule auto_rule_20250726141031_8115 {
  strings:
    $o0 = "dword_402FA0" wide ascii nocase
    $o1 = "word_40309C" wide ascii nocase
  condition:
    all of them
}