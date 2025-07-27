rule auto_rule_20250726130754_9617 {
  strings:
    $o0 = "dword_78108" wide ascii nocase
    $o1 = "dword_77EF0" wide ascii nocase
  condition:
    all of them
}