rule auto_rule_20250726204303_9210 {
  strings:
    $o0 = "x77BBC2A7u" wide ascii nocase
  condition:
    all of them
}