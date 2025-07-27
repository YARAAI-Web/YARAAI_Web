rule auto_rule_20250726100649_9776 {
  strings:
    $o0 = "_CrtMemCheckPoint" wide ascii nocase
  condition:
    all of them
}