rule auto_rule_20250727041402_3975 {
  strings:
    $o0 = "dword_4C1294" wide ascii nocase
  condition:
    all of them
}