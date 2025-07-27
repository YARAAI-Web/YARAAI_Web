rule auto_rule_20250726101906_7489 {
  strings:
    $o0 = "dword_42823F" wide ascii nocase
    $o1 = "x1CD5u" wide ascii nocase
    $o2 = "B9Eh" wide ascii nocase
  condition:
    3 of ($o*)
}