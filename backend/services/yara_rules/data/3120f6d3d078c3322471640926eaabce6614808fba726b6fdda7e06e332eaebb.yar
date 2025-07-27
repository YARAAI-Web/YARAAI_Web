rule auto_rule_20250727041258_6476 {
  strings:
    $o0 = "dword_45CAC8" wide ascii nocase
  condition:
    all of them
}