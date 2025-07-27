rule auto_rule_20250727040256_9062 {
  strings:
    $o0 = "x751C80u" wide ascii nocase
    $o1 = "dword_42A87D" wide ascii nocase
  condition:
    all of them
}