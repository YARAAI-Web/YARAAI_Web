rule auto_rule_20250727033151_3847 {
  strings:
    $o0 = "_close" wide ascii nocase
    $o1 = "TrailDown2" wide ascii nocase
    $o2 = "dword_463A20" wide ascii nocase
    $o3 = "dword_464270" wide ascii nocase
  condition:
    4 of ($o*)
}