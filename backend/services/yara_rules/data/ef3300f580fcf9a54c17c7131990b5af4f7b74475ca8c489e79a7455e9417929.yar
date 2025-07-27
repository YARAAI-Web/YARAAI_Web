rule auto_rule_20250727005235_1948 {
  strings:
    $o0 = "dword_4C12DC" wide ascii nocase
    $o1 = "dword_4C15D8" wide ascii nocase
  condition:
    all of them
}