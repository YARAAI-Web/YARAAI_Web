rule auto_rule_20250726102911_2538 {
  strings:
    $o0 = "dword_4C1304" wide ascii nocase
    $o1 = "dword_4C10BC" wide ascii nocase
  condition:
    all of them
}