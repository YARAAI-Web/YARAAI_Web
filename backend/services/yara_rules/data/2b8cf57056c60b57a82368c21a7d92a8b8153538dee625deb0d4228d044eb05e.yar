rule auto_rule_20250726164934_7736 {
  strings:
    $o0 = "word_401E72" wide ascii nocase
  condition:
    all of them
}