rule auto_rule_20250726115054_9794 {
  strings:
    $o0 = "x71A5u" wide ascii nocase
    $o1 = "x3339u" wide ascii nocase
  condition:
    all of them
}