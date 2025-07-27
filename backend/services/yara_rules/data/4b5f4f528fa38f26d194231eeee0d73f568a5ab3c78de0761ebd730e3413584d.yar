rule auto_rule_20250727001135_2354 {
  strings:
    $o0 = "_ZeroTail" wide ascii nocase
    $o1 = "off_456060" wide ascii nocase
  condition:
    all of them
}