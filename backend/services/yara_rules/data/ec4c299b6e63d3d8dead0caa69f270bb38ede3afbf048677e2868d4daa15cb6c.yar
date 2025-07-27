rule auto_rule_20250727043116_8677 {
  strings:
    $o0 = "dword_6502E060" wide ascii nocase
    $o1 = "TargetHandle" wide ascii nocase
  condition:
    all of them
}