rule auto_rule_20250726162722_5415 {
  strings:
    $o0 = "dword_4282BB" wide ascii nocase
    $o1 = "x329E695Du" wide ascii nocase
    $o2 = "x528B" wide ascii nocase
    $o3 = "dword_4282CB" wide ascii nocase
    $o4 = "C06h" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726162725_7640 {
  strings:
    $o0 = "xCA79A577" wide ascii nocase
    $o1 = "x3A7C00000000LL" wide ascii nocase
    $o2 = "x42226F" wide ascii nocase
    $o3 = "BF6h" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726162729_4073 {
  condition:
    auto_rule_20250726162722_5415 or auto_rule_20250726162725_7640
}