rule auto_rule_20250726111500_1761 {
  strings:
    $o0 = "copy_start" wide ascii nocase
    $o1 = "UnwindUp4_0" wide ascii nocase
    $o2 = "dword_45D558" wide ascii nocase
    $o3 = "dword_45D540" wide ascii nocase
  condition:
    4 of ($o*)
}