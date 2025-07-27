rule auto_rule_20250726074908_7136 {
  strings:
    $o0 = "word_650266DC" wide ascii nocase
  condition:
    all of them
}