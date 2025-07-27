rule auto_rule_20250726162103_4835 {
  strings:
    $o0 = "qword_140032068" wide ascii nocase
  condition:
    all of them
}