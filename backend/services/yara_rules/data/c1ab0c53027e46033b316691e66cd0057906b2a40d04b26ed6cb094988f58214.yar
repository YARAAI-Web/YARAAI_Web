rule auto_rule_20250726191533_1127 {
  strings:
    $o0 = "word_401EBA" wide ascii nocase
  condition:
    all of them
}