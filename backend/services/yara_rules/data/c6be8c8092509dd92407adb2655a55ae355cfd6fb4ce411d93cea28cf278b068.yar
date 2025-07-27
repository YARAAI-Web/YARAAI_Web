rule auto_rule_20250727001958_0308 {
  strings:
    $o0 = "word_4C12D4" wide ascii nocase
  condition:
    all of them
}