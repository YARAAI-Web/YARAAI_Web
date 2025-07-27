rule auto_rule_20250726220038_6521 {
  strings:
    $o0 = "x66FC" wide ascii nocase
    $o1 = "PulseEvent" wide ascii nocase
  condition:
    all of them
}