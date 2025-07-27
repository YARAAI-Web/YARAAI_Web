rule auto_rule_20250726093309_1624 {
  strings:
    $o0 = "ReleaseMutex_0" wide ascii nocase
  condition:
    all of them
}