rule auto_rule_20250726173536_2916 {
  strings:
    $o0 = "x5059" wide ascii nocase
    $o1 = "dword_435E42" wide ascii nocase
  condition:
    all of them
}