rule auto_rule_20250727015023_8412 {
  strings:
    $o0 = "_Locimp_dtor" wide ascii nocase
    $o1 = "dword_10036034" wide ascii nocase
  condition:
    all of them
}