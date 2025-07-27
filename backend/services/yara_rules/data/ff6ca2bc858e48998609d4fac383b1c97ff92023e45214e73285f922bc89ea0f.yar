rule auto_rule_20250726232950_4699 {
  strings:
    $o0 = "qword_140043FC0" wide ascii nocase
    $o1 = "x3090u" wide ascii nocase
  condition:
    all of them
}