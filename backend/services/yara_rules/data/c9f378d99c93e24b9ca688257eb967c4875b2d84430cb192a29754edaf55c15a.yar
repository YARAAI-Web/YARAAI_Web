rule auto_rule_20250726063855_6570 {
  strings:
    $o0 = "UnwindUp4_0" wide ascii nocase
    $o1 = "dword_411EE4" wide ascii nocase
    $o2 = "VirtualFree" wide ascii nocase
  condition:
    3 of ($o*)
}