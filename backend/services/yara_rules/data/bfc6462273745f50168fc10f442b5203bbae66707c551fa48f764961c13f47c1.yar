rule auto_rule_20250726090314_5994 {
  strings:
    $o0 = "dword_40CE14" wide ascii nocase
    $o1 = "dbl_40CB08" wide ascii nocase
  condition:
    all of them
}