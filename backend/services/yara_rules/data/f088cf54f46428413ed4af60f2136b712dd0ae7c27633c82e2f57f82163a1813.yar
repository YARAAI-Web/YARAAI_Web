rule auto_rule_20250726234336_7211 {
  strings:
    $o0 = "dword_46442C" wide ascii nocase
    $o1 = "dword_463B08" wide ascii nocase
    $o2 = "_cinit" wide ascii nocase
  condition:
    3 of ($o*)
}