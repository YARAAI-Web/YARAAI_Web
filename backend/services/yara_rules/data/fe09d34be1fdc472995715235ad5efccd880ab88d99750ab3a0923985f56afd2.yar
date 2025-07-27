rule auto_rule_20250726075849_6658 {
  strings:
    $o0 = "dword_446DA8" wide ascii nocase
    $o1 = "dword_4466D0" wide ascii nocase
    $o2 = "UnwindUp0_0" wide ascii nocase
    $o3 = "_bittestandset" wide ascii nocase
    $o4 = "UnwindUp2_0" wide ascii nocase
  condition:
    4 of ($o*)
}