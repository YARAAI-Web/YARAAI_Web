rule auto_rule_20250727043700_1396 {
  strings:
    $o0 = "dword_4693F0" wide ascii nocase
    $o1 = "dword_467760" wide ascii nocase
  condition:
    all of them
}