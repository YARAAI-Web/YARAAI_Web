rule auto_rule_20250727014934_0471 {
  strings:
    $o0 = "dword_64030368" wide ascii nocase
  condition:
    all of them
}