rule auto_rule_20250726221722_2932 {
  strings:
    $o0 = "dword_45CFC8" wide ascii nocase
    $o1 = "dword_45D8A8" wide ascii nocase
  condition:
    all of them
}