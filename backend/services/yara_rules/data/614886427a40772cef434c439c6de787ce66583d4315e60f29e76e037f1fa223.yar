rule auto_rule_20250726234021_2378 {
  strings:
    $o0 = "_abnormal_termination" wide ascii nocase
    $o1 = "_wincmdln" wide ascii nocase
    $o2 = "__sbh_alloc_new_region" wide ascii nocase
    $o3 = "dword_411EAC" wide ascii nocase
    $o4 = "UnwindUp6_0" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250726234024_8690 {
  strings:
    $o0 = "dword_411D48" wide ascii nocase
    $o1 = "dword_411D4C" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726234036_6658 {
  condition:
    auto_rule_20250726234021_2378 or auto_rule_20250726234024_8690
}