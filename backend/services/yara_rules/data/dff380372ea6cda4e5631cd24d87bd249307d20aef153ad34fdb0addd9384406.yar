rule auto_rule_20250727013758_7240 {
  strings:
    $o0 = "dword_42EED4" wide ascii nocase
  condition:
    all of them
}