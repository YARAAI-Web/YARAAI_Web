rule auto_rule_20250727044727_0016 {
  strings:
    $o0 = "dword_427CD4" wide ascii nocase
    $o1 = "tMIXERCONTROLDETAILS" wide ascii nocase
    $o2 = "dword_427CA0" wide ascii nocase
    $o3 = "CodePagea" wide ascii nocase
    $o4 = "dword_4280A8" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727044730_7612 {
  strings:
    $o0 = "_cinit" wide ascii nocase
    $o1 = "dword_4281E8" wide ascii nocase
    $o2 = "__shr_12" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250727044734_8375 {
  condition:
    auto_rule_20250727044727_0016 or auto_rule_20250727044730_7612
}