rule auto_rule_20250726152703_5213 {
  strings:
    $o0 = "dword_78380" wide ascii nocase
  condition:
    all of them
}