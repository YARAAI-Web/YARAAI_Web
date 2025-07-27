rule auto_rule_20250726215505_2489 {
  strings:
    $o0 = "dword_417C98" wide ascii nocase
  condition:
    all of them
}