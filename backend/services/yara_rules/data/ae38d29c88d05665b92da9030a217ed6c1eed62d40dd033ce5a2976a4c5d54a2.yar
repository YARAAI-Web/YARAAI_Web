rule auto_rule_20250727012707_1083 {
  strings:
    $o0 = "dword_6402E990" wide ascii nocase
  condition:
    all of them
}