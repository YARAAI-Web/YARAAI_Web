rule auto_rule_20250727021834_1975 {
  strings:
    $o0 = "dword_4574D0" wide ascii nocase
  condition:
    all of them
}