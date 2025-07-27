rule auto_rule_20250727002008_2841 {
  strings:
    $o0 = "dword_6402F540" wide ascii nocase
  condition:
    all of them
}