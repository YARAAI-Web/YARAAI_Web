rule auto_rule_20250727003528_9710 {
  strings:
    $o0 = "dword_4479E4" wide ascii nocase
  condition:
    all of them
}