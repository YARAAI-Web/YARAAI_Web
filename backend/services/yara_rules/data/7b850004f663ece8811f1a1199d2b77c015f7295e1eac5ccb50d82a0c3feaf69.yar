rule auto_rule_20250726074740_7921 {
  strings:
    $o0 = "word_140066BEE" wide ascii nocase
  condition:
    all of them
}