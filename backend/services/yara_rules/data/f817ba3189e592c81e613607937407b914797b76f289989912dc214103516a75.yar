rule auto_rule_20250727003332_9191 {
  strings:
    $o0 = "qword_140003C90" wide ascii nocase
  condition:
    all of them
}