rule auto_rule_20250727034933_7112 {
  strings:
    $o0 = "dword_6402E98C" wide ascii nocase
  condition:
    all of them
}