rule auto_rule_20250727041206_6751 {
  strings:
    $o0 = "x5145u" wide ascii nocase
    $o1 = "dword_417E3D" wide ascii nocase
    $o2 = "dword_4245AE" wide ascii nocase
    $o3 = "dword_417E41" wide ascii nocase
  condition:
    4 of ($o*)
}