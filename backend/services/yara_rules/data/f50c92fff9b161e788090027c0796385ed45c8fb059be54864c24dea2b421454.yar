rule auto_rule_20250726204205_6189 {
  strings:
    $o0 = "aTerminateproce" wide ascii nocase
  condition:
    all of them
}