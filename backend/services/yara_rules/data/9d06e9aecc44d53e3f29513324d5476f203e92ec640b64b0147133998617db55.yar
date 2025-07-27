rule auto_rule_20250727040814_9095 {
  strings:
    $o0 = "dword_6402E984" wide ascii nocase
  condition:
    all of them
}