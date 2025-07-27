rule auto_rule_20250726165240_9329 {
  strings:
    $o0 = "dword_6D1360" wide ascii nocase
  condition:
    all of them
}