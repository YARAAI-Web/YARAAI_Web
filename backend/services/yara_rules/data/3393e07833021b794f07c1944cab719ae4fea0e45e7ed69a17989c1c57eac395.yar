rule auto_rule_20250726214344_2262 {
  strings:
    $o0 = "dword_40A5A8" wide ascii nocase
    $o1 = "dword_4100B7" wide ascii nocase
    $o2 = "dword_40A5A0" wide ascii nocase
    $o3 = "xFDEu" wide ascii nocase
    $o4 = "dword_40A608" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726214348_5062 {
  strings:
    $o0 = "dword_40A5AC" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726214352_4616 {
  condition:
    auto_rule_20250726214344_2262 or auto_rule_20250726214348_5062
}