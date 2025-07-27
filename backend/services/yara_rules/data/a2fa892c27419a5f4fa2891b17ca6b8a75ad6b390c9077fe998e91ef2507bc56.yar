rule auto_rule_20250726081343_2485 {
  strings:
    $o0 = "dword_64030370" wide ascii nocase
  condition:
    all of them
}