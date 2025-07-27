rule auto_rule_20250727043825_5311 {
  strings:
    $o0 = "qword_180508978" wide ascii nocase
  condition:
    all of them
}