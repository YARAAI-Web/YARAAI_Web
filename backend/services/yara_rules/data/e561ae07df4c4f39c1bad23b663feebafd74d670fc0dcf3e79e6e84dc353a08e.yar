rule auto_rule_20250727043028_4382 {
  strings:
    $o0 = "dword_411A44" wide ascii nocase
    $o1 = "byte_4120C1" wide ascii nocase
    $o2 = "LoadBitmapA" wide ascii nocase
    $o3 = "off_411A64" wide ascii nocase
    $o4 = "UnwindUp1_0" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727043031_2476 {
  strings:
    $o0 = "dword_411F6C" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727043036_7043 {
  condition:
    auto_rule_20250727043028_4382 or auto_rule_20250727043031_2476
}