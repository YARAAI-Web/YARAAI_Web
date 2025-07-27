rule auto_rule_20250726101856_5776 {
  strings:
    $o0 = "lpMaxMessageSize" wide ascii nocase
  condition:
    all of them
}