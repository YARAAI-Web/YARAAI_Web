rule auto_rule_20250726192928_4908 {
  strings:
    $o0 = "qword_40A764" wide ascii nocase
    $o1 = "x7BFB" wide ascii nocase
    $o2 = "dword_41009F" wide ascii nocase
    $o3 = "dword_40A730" wide ascii nocase
    $o4 = "dword_40A5B8" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726192931_0149 {
  strings:
    $o0 = "off_40A384" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726192934_1113 {
  condition:
    auto_rule_20250726192928_4908 or auto_rule_20250726192931_0149
}