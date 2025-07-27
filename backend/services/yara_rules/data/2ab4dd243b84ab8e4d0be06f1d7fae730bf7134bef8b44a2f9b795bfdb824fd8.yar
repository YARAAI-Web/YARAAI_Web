rule auto_rule_20250726201640_2150 {
  strings:
    $o0 = "word_1E6EA" wide ascii nocase
  condition:
    all of them
}