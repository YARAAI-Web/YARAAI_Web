rule auto_rule_20250726124922_9568 {
  strings:
    $o0 = "off_467520" wide ascii nocase
  condition:
    all of them
}