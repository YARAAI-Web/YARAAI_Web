rule auto_rule_20250727034815_6033 {
  strings:
    $o0 = "dword_503004" wide ascii nocase
  condition:
    all of them
}