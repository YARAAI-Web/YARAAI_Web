rule auto_rule_20250726152535_6199 {
  strings:
    $o0 = "word_1C0CE" wide ascii nocase
  condition:
    all of them
}