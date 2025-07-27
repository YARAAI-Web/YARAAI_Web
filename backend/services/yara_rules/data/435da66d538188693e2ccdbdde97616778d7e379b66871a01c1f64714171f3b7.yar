rule auto_rule_20250727003020_8515 {
  strings:
    $o0 = "pSessionId" wide ascii nocase
    $o1 = "iMaxLength" wide ascii nocase
  condition:
    all of them
}