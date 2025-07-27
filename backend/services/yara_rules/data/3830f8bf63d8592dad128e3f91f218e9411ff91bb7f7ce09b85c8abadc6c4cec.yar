rule auto_rule_20250727044436_9077 {
  strings:
    $o0 = "dword_64030360" wide ascii nocase
  condition:
    all of them
}