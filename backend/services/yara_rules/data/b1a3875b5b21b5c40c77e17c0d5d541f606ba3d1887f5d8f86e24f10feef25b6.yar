rule auto_rule_20250726212736_5298 {
  strings:
    $o0 = "qword_1803BB328" wide ascii nocase
  condition:
    all of them
}