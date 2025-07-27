rule auto_rule_20250726082529_7483 {
  strings:
    $o0 = "word_1E60E" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}