rule auto_rule_20250726174033_0096 {
  strings:
    $o0 = "dword_44E5CC" wide ascii nocase
    $o1 = "dword_44E1A4" wide ascii nocase
  condition:
    all of them
}