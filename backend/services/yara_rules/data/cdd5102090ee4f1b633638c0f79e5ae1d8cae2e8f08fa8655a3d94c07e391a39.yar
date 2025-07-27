rule auto_rule_20250726091224_5400 {
  strings:
    $o0 = "qword_140043EC8" wide ascii nocase
    $o1 = "lambda" wide ascii nocase
  condition:
    all of them
}