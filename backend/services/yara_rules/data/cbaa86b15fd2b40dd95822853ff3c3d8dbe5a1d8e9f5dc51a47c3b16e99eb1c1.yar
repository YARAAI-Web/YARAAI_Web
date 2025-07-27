rule auto_rule_20250727040720_7583 {
  strings:
    $o0 = "qword_140043E18" wide ascii nocase
  condition:
    all of them
}