rule auto_rule_20250726103024_8897 {
  strings:
    $o0 = "qword_2457B9910" wide ascii nocase
  condition:
    all of them
}