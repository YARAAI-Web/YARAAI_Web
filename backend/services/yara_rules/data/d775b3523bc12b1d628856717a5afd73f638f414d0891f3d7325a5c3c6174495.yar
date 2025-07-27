rule auto_rule_20250726163707_5123 {
  strings:
    $o0 = "word_401EBE" wide ascii nocase
  condition:
    all of them
}