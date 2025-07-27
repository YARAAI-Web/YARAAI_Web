rule auto_rule_20250726063313_3853 {
  strings:
    $o0 = "dword_65030404" wide ascii nocase
  condition:
    all of them
}