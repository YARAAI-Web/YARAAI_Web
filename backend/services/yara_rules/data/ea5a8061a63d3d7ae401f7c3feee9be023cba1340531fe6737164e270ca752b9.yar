rule auto_rule_20250727005635_7624 {
  strings:
    $o0 = "aStftware" wide ascii nocase
  condition:
    all of them
}