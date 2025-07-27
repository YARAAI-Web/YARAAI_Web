rule auto_rule_20250726122009_7798 {
  strings:
    $o0 = "qword_180E86430" wide ascii nocase
  condition:
    all of them
}