rule auto_rule_20250726194458_8589 {
  strings:
    $o0 = "word_1E762" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}