rule auto_rule_20250726103117_5546 {
  strings:
    $o0 = "dword_43B436" wide ascii nocase
    $o1 = "dword_43B44D" wide ascii nocase
    $o2 = "dword_43B245" wide ascii nocase
    $o3 = "dword_43B1E9" wide ascii nocase
    $o4 = "dword_43B08A" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726103120_2868 {
  strings:
    $o0 = "dword_43B0D6" wide ascii nocase
    $o1 = "dword_43B162" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726103124_9197 {
  condition:
    auto_rule_20250726103117_5546 or auto_rule_20250726103120_2868
}