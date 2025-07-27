rule auto_rule_20250726125125_0879 {
  strings:
    $o0 = "ReturnValue" wide ascii nocase
    $o1 = "dword_45AE24" wide ascii nocase
    $o2 = "dword_45B144" wide ascii nocase
    $o3 = "dword_45A990" wide ascii nocase
  condition:
    4 of ($o*)
}