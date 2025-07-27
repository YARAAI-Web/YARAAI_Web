rule auto_rule_20250726112421_8508 {
  strings:
    $o0 = "byte_64030190" wide ascii nocase
    $o1 = "word_64026604" wide ascii nocase
  condition:
    all of them
}