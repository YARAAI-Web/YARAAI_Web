rule auto_rule_20250726222237_6563 {
  strings:
    $o0 = "TrailDown2" wide ascii nocase
    $o1 = "dword_45D178" wide ascii nocase
    $o2 = "dword_45D53C" wide ascii nocase
    $o3 = "UnwindUp0_0" wide ascii nocase
  condition:
    4 of ($o*)
}