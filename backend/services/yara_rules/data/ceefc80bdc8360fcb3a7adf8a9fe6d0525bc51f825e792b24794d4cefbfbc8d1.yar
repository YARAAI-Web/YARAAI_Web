rule auto_rule_20250726230854_6662 {
  strings:
    $o0 = "_mtdeletelocks" wide ascii nocase
    $o1 = "PatBlt" wide ascii nocase
    $o2 = "dword_4548E0" wide ascii nocase
    $o3 = "UnwindUp0_0" wide ascii nocase
  condition:
    4 of ($o*)
}