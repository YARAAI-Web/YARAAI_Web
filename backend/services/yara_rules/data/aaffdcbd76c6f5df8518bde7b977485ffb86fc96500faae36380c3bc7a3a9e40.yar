rule auto_rule_20250726081929_9043 {
  strings:
    $o0 = "word_44E710" wide ascii nocase
  condition:
    all of them
}