rule auto_rule_20250726152558_3086 {
  strings:
    $o0 = "word_1E992" wide ascii nocase
  condition:
    all of them
}