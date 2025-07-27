rule auto_rule_20250726201653_1705 {
  strings:
    $o0 = "dword_43B16F" wide ascii nocase
    $o1 = "x2940A200u" wide ascii nocase
    $o2 = "x65B5C" wide ascii nocase
    $o3 = "dword_43B48B" wide ascii nocase
    $o4 = "dword_43B5AE" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726201656_2733 {
  strings:
    $o0 = "dword_43B253" wide ascii nocase
    $o1 = "dword_43B024" wide ascii nocase
    $o2 = "dword_43B3F2" wide ascii nocase
    $o3 = "dword_43B6F7" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726201700_5180 {
  condition:
    auto_rule_20250726201653_1705 or auto_rule_20250726201656_2733
}