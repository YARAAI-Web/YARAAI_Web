rule auto_rule_20250726071130_2041 {
  strings:
    $o0 = "wHow" wide ascii nocase
    $o1 = "GetProcessTimes" wide ascii nocase
  condition:
    all of them
}