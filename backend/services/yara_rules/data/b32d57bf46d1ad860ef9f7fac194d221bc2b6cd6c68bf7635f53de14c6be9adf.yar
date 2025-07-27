rule auto_rule_20250727032500_7669 {
  strings:
    $o0 = "_positive" wide ascii nocase
    $o1 = "dword_456D34" wide ascii nocase
  condition:
    all of them
}