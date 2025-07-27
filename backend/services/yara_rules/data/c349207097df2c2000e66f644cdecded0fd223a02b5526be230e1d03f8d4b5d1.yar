rule auto_rule_20250726222840_0606 {
  strings:
    $o0 = "algn_405472" wide ascii nocase
  condition:
    all of them
}