rule auto_rule_20250726124313_0725 {
  strings:
    $o0 = "word_1E682" wide ascii nocase
  condition:
    all of them
}