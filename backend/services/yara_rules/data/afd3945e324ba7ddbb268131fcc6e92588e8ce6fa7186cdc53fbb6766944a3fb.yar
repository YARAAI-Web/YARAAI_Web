rule auto_rule_20250727031553_1281 {
  strings:
    $o0 = "ReleaseMutex_0" wide ascii nocase
  condition:
    all of them
}