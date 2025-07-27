rule auto_rule_20250726205017_8952 {
  strings:
    $o0 = "dword_1001D258" wide ascii nocase
  condition:
    all of them
}