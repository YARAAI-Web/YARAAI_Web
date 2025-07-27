rule auto_rule_20250727044749_6110 {
  strings:
    $o0 = "dword_64031328" wide ascii nocase
  condition:
    all of them
}