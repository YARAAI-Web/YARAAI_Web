rule auto_rule_20250726075124_9837 {
  strings:
    $o0 = "dword_426F25" wide ascii nocase
  condition:
    all of them
}