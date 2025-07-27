rule auto_rule_20250726132613_5422 {
  strings:
    $o0 = "dword_45C1C4" wide ascii nocase
    $o1 = "word_42893A" wide ascii nocase
  condition:
    all of them
}