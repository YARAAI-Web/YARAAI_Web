rule auto_rule_20250727032348_3121 {
  strings:
    $o0 = "qword_18014ACC0" wide ascii nocase
    $o1 = "qword_18026D8B0" wide ascii nocase
  condition:
    all of them
}