rule auto_rule_20250726232223_9084 {
  strings:
    $o0 = "x2176" wide ascii nocase
    $o1 = "x4495" wide ascii nocase
  condition:
    all of them
}