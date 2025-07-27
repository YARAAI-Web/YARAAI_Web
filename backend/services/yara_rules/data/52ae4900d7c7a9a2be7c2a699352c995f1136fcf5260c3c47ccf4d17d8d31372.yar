rule auto_rule_20250727044705_0982 {
  strings:
    $o0 = "dword_783E4" wide ascii nocase
  condition:
    all of them
}