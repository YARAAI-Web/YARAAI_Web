rule auto_rule_20250726165231_6203 {
  strings:
    $o0 = "x8E93D2A3" wide ascii nocase
  condition:
    all of them
}