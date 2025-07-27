rule auto_rule_20250727034519_0067 {
  strings:
    $o0 = "dword_1400D143C" wide ascii nocase
  condition:
    all of them
}