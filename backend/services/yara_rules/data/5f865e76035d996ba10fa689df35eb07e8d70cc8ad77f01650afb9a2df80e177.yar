rule auto_rule_20250726124324_3921 {
  strings:
    $o0 = "dword_417570" wide ascii nocase
    $o1 = "x15500u" wide ascii nocase
  condition:
    all of them
}