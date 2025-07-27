rule auto_rule_20250727000217_6460 {
  strings:
    $o0 = "xF89C85BA" wide ascii nocase
    $o1 = "dword_428EAD" wide ascii nocase
  condition:
    all of them
}