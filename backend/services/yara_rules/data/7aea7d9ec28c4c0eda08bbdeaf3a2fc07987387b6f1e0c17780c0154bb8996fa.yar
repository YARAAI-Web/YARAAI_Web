rule auto_rule_20250726152402_2546 {
  strings:
    $o0 = "TextOutA" wide ascii nocase
    $o1 = "dword_42EF10" wide ascii nocase
    $o2 = "dword_430586" wide ascii nocase
    $o3 = "SetSystem" wide ascii nocase
    $o4 = "cAccel" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726152405_1731 {
  strings:
    $o0 = "x57EB0032729DLL" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726152408_3899 {
  condition:
    auto_rule_20250726152402_2546 or auto_rule_20250726152405_1731
}