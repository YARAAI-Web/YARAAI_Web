rule auto_rule_20250726210151_6579 {
  strings:
    $o0 = "dword_412238" wide ascii nocase
    $o1 = "dword_40E004" wide ascii nocase
  condition:
    all of them
}