rule auto_rule_20250726060256_1674 {
  strings:
    $o0 = "dword_4C115C" wide ascii nocase
    $o1 = "dword_4C1310" wide ascii nocase
  condition:
    all of them
}