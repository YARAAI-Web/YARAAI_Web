rule auto_rule_20250726205029_8586 {
  strings:
    $o0 = "dword_78308" wide ascii nocase
    $o1 = "dword_78484" wide ascii nocase
  condition:
    all of them
}