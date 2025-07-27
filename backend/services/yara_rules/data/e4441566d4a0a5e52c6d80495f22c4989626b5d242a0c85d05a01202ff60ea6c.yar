rule auto_rule_20250726155446_7133 {
  strings:
    $o0 = "word_460502" wide ascii nocase
  condition:
    all of them
}