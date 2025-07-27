rule auto_rule_20250726124406_9045 {
  strings:
    $o0 = "lpProcessAttributes" wide ascii nocase
    $o1 = "GetCommState" wide ascii nocase
  condition:
    all of them
}