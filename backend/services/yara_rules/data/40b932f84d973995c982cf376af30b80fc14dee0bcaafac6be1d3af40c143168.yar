rule auto_rule_20250726222952_9218 {
  strings:
    $o0 = "x17000u" wide ascii nocase
  condition:
    all of them
}