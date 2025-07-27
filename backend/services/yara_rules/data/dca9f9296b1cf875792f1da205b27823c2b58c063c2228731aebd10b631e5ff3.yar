rule auto_rule_20250727041423_2288 {
  strings:
    $o0 = "dword_40B844" wide ascii nocase
  condition:
    all of them
}