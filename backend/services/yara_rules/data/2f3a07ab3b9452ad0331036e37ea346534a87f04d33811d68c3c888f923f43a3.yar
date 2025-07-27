rule auto_rule_20250726183936_4992 {
  strings:
    $o0 = "VirtualFree" wide ascii nocase
    $o1 = "TrailDown1_0" wide ascii nocase
    $o2 = "UnwindUp4_0" wide ascii nocase
    $o3 = "dword_445EAC" wide ascii nocase
  condition:
    4 of ($o*)
}