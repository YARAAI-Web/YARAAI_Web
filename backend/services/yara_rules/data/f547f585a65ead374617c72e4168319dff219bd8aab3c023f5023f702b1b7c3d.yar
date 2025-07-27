rule auto_rule_20250727032018_0962 {
  strings:
    $o0 = "ReleaseMutex_0" wide ascii nocase
  condition:
    all of them
}