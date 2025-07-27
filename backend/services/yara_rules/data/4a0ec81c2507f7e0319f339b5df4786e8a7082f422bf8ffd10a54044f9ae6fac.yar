rule auto_rule_20250726085313_2370 {
  strings:
    $o0 = "EnumPropsA" wide ascii nocase
    $o1 = "lpMenuName" wide ascii nocase
  condition:
    all of them
}