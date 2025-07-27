rule auto_rule_20250727011634_0918 {
  strings:
    $o0 = "dword_41FFB0" wide ascii nocase
  condition:
    all of them
}