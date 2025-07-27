rule auto_rule_20250727021958_8042 {
  strings:
    $o0 = "dword_6402E994" wide ascii nocase
  condition:
    all of them
}