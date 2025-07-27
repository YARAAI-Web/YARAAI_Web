rule auto_rule_20250726093558_9154 {
  strings:
    $o0 = "Press" wide ascii nocase
    $o1 = "dword_446BEC" wide ascii nocase
  condition:
    all of them
}