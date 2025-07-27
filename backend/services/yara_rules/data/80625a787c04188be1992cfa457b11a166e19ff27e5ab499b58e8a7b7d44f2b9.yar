rule auto_rule_20250727033618_5198 {
  strings:
    $o0 = "dword_13CF29A0" wide ascii nocase
  condition:
    all of them
}