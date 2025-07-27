rule auto_rule_20250727022913_0364 {
  strings:
    $o0 = "x401981" wide ascii nocase
    $o1 = "xB5412650" wide ascii nocase
  condition:
    all of them
}