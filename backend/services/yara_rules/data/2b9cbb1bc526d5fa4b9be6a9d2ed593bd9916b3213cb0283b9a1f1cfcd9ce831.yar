rule auto_rule_20250726115328_7518 {
  strings:
    $o0 = "dword_40320C" wide ascii nocase
  condition:
    all of them
}