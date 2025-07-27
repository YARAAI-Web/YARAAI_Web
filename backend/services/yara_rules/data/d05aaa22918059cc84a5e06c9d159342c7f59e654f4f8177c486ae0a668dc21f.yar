rule auto_rule_20250726231747_2089 {
  strings:
    $o0 = "x4036C1" wide ascii nocase
    $o1 = "UnwindUp2_0" wide ascii nocase
  condition:
    all of them
}