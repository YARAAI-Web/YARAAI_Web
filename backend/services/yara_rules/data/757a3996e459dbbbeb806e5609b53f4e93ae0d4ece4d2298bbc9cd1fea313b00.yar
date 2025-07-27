rule auto_rule_20250727031731_2131 {
  strings:
    $o0 = "qword_18021BCE8" wide ascii nocase
    $o1 = "qword_18021B7C0" wide ascii nocase
  condition:
    all of them
}