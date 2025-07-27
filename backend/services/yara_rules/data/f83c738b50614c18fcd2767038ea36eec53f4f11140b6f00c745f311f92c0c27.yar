rule auto_rule_20250727033736_8669 {
  strings:
    $o0 = "dword_4C18AC" wide ascii nocase
  condition:
    all of them
}