rule auto_rule_20250727032740_7506 {
  strings:
    $o0 = "aInconsistentIo" wide ascii nocase
  condition:
    all of them
}