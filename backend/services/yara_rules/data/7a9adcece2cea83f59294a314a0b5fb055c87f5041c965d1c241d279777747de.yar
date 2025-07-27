rule auto_rule_20250727021749_6374 {
  strings:
    $o0 = "off_409FBC" wide ascii nocase
    $o1 = "j_j_j_nullsub_28_0_0" wide ascii nocase
    $o2 = "xC06D007F" wide ascii nocase
    $o3 = "dword_4FDDD8" wide ascii nocase
  condition:
    4 of ($o*)
}