rule auto_rule_20250727010718_7847 {
  strings:
    $o0 = "dword_4C1314" wide ascii nocase
  condition:
    all of them
}