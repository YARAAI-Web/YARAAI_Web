rule auto_rule_20250726173401_9160 {
  strings:
    $o0 = "aMqa44e2xIb" wide ascii nocase
  condition:
    all of them
}