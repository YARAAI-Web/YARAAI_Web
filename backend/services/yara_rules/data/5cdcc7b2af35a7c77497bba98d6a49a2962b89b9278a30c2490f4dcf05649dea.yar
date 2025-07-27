rule auto_rule_20250726134927_6408 {
  strings:
    $o0 = "nResult" wide ascii nocase
    $o1 = "SetCalendarInfoA" wide ascii nocase
  condition:
    all of them
}