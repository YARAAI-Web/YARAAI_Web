rule auto_rule_20250726212626_5330 {
  strings:
    $o0 = "qword_140043F28" wide ascii nocase
  condition:
    all of them
}