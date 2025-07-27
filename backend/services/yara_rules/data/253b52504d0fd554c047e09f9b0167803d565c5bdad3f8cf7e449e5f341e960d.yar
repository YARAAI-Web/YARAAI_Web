rule auto_rule_20250726142243_5636 {
  strings:
    $o0 = "word_1EB62" wide ascii nocase
    $o1 = "dword_785A4" wide ascii nocase
  condition:
    all of them
}