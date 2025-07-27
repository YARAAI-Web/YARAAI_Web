rule auto_rule_20250726101926_7489 {
  strings:
    $o0 = "dword_64031354" wide ascii nocase
    $o1 = "lpThreadParameter" wide ascii nocase
  condition:
    all of them
}