rule auto_rule_20250726150259_9287 {
  strings:
    $o0 = "qword_1402BBA90" wide ascii nocase
  condition:
    all of them
}