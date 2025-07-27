rule auto_rule_20250727020436_3281 {
  strings:
    $o0 = "x15500u" wide ascii nocase
    $o1 = "lpKeyState" wide ascii nocase
  condition:
    all of them
}