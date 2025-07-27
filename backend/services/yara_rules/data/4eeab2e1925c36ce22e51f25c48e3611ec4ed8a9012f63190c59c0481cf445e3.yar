rule auto_rule_20250726082756_8153 {
  strings:
    $o0 = "dword_43B3A3" wide ascii nocase
    $o1 = "dword_43B7B3" wide ascii nocase
    $o2 = "dword_43B473" wide ascii nocase
    $o3 = "dword_43B8CA" wide ascii nocase
    $o4 = "aOoeqtw34466Bcn" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726082759_9554 {
  strings:
    $o0 = "dword_43B40A" wide ascii nocase
    $o1 = "dword_43B670" wide ascii nocase
    $o2 = "x495B4500" wide ascii nocase
    $o3 = "dword_43B38B" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726082803_5925 {
  condition:
    auto_rule_20250726082756_8153 or auto_rule_20250726082759_9554
}