rule auto_rule_20250726200424_2270 {
  strings:
    $o0 = "qword_140050248" wide ascii nocase
  condition:
    all of them
}