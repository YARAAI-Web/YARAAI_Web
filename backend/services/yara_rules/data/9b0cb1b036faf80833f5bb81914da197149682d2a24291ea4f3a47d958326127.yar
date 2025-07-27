rule auto_rule_20250727003226_4646 {
  strings:
    $o0 = "dword_64031354" wide ascii nocase
  condition:
    all of them
}