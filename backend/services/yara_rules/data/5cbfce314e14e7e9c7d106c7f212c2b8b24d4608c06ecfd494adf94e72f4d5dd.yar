rule auto_rule_20250726084546_1315 {
  strings:
    $o0 = "dword_469B70" wide ascii nocase
    $o1 = "byte_469E81" wide ascii nocase
  condition:
    all of them
}