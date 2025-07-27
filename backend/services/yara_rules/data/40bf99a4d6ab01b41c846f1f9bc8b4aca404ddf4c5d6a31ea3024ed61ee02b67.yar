rule auto_rule_20250726084645_4497 {
  strings:
    $o0 = "word_64026644" wide ascii nocase
  condition:
    all of them
}