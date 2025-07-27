rule auto_rule_20250727001638_3438 {
  strings:
    $o0 = "dword_4C1740" wide ascii nocase
  condition:
    all of them
}