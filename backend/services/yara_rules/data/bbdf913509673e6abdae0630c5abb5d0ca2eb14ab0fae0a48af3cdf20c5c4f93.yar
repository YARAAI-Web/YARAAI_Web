rule auto_rule_20250726172916_0753 {
  strings:
    $o0 = "dword_43B448" wide ascii nocase
    $o1 = "dword_43B670" wide ascii nocase
    $o2 = "x65B5C" wide ascii nocase
    $o3 = "dword_43B4CF" wide ascii nocase
    $o4 = "dword_43B203" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726172920_1037 {
  strings:
    $o0 = "dword_43B643" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726172923_7956 {
  condition:
    auto_rule_20250726172916_0753 or auto_rule_20250726172920_1037
}