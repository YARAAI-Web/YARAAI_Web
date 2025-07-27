rule auto_rule_20250727005604_7143 {
  strings:
    $o0 = "dword_1E528" wide ascii nocase
  condition:
    all of them
}