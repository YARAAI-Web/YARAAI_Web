rule auto_rule_20250726182900_5434 {
  strings:
    $o0 = "dword_4162EC" wide ascii nocase
    $o1 = "dword_41656D" wide ascii nocase
    $o2 = "dword_4162E8" wide ascii nocase
    $o3 = "x3913u" wide ascii nocase
  condition:
    4 of ($o*)
}