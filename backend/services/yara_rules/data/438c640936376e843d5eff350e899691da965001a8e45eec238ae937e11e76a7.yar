rule auto_rule_20250726130513_0485 {
  strings:
    $o0 = "dword_6402E984" wide ascii nocase
  condition:
    all of them
}