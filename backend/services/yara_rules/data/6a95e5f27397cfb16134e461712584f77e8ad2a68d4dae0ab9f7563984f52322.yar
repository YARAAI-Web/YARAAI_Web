rule auto_rule_20250727032336_0129 {
  strings:
    $o0 = "aInconsistentIo" wide ascii nocase
  condition:
    all of them
}