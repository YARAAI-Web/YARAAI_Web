rule auto_rule_20250727012445_8105 {
  strings:
    $o0 = "dword_411F08" wide ascii nocase
    $o1 = "dword_411D84" wide ascii nocase
  condition:
    all of them
}