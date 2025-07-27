rule auto_rule_20250726132515_9798 {
  strings:
    $o0 = "x65B3F" wide ascii nocase
    $o1 = "dword_43B3D2" wide ascii nocase
    $o2 = "dword_43B510" wide ascii nocase
    $o3 = "dword_43B2CC" wide ascii nocase
    $o4 = "dword_43B10C" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726132518_5315 {
  strings:
    $o0 = "dword_43B502" wide ascii nocase
    $o1 = "dword_43B7B3" wide ascii nocase
    $o2 = "dword_43B3C1" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726132521_0949 {
  condition:
    auto_rule_20250726132515_9798 or auto_rule_20250726132518_5315
}