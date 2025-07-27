rule auto_rule_20250726102645_7840 {
  strings:
    $o0 = "u_long" wide ascii nocase
    $o1 = "dwErrCodea" wide ascii nocase
    $o2 = "F60h" wide ascii nocase
    $o3 = "dword_6402F190" wide ascii nocase
  condition:
    4 of ($o*)
}