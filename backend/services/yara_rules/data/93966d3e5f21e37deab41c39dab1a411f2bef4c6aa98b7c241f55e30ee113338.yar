rule auto_rule_20250727003215_5047 {
  strings:
    $o0 = "dword_4638BC" wide ascii nocase
    $o1 = "x41C4u" wide ascii nocase
  condition:
    all of them
}