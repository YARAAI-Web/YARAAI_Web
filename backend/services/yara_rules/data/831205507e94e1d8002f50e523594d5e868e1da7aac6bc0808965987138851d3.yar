rule auto_rule_20250727013002_1594 {
  strings:
    $o0 = "x7FD4u" wide ascii nocase
    $o1 = "xA2008210" wide ascii nocase
  condition:
    all of them
}