rule auto_rule_20250726173729_2399 {
  strings:
    $o0 = "dword_45CEEC" wide ascii nocase
  condition:
    all of them
}