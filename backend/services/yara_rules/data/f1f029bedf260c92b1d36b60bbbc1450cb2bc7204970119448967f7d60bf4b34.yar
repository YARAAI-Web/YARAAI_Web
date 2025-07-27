rule auto_rule_20250726114504_0831 {
  strings:
    $o0 = "word_460500" wide ascii nocase
  condition:
    all of them
}