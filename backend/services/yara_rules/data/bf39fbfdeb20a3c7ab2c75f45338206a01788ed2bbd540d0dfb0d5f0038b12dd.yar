rule auto_rule_20250727020321_9228 {
  strings:
    $o0 = "x4036D1" wide ascii nocase
    $o1 = "gu_return" wide ascii nocase
  condition:
    all of them
}