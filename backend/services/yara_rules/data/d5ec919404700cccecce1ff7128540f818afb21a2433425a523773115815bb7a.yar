rule auto_rule_20250727022643_3102 {
  strings:
    $o0 = "qword_14018C6A0" wide ascii nocase
  condition:
    all of them
}