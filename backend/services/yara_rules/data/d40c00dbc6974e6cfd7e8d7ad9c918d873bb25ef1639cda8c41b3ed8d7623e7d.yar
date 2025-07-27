rule auto_rule_20250726092054_0858 {
  strings:
    $o0 = "dword_101CE2A8" wide ascii nocase
  condition:
    all of them
}