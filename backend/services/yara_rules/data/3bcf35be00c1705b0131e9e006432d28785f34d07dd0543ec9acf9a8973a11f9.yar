rule auto_rule_20250726222246_9485 {
  strings:
    $o0 = "word_475BF0" wide ascii nocase
  condition:
    all of them
}