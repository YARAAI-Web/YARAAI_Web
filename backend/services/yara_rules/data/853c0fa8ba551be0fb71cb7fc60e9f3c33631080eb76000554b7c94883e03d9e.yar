rule auto_rule_20250726203444_1314 {
  strings:
    $o0 = "strcat" wide ascii nocase
    $o1 = "dword_44BEA0" wide ascii nocase
  condition:
    all of them
}