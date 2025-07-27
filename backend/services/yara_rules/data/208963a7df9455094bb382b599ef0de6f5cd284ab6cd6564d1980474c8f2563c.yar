rule auto_rule_20250726224042_8529 {
  strings:
    $o0 = "dword_450564" wide ascii nocase
    $o1 = "GetStringTypeW" wide ascii nocase
    $o2 = "strcspn" wide ascii nocase
    $o3 = "dword_451290" wide ascii nocase
    $o4 = "gu_return" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726224045_5119 {
  strings:
    $o0 = "dword_450FB8" wide ascii nocase
    $o1 = "dword_451114" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726224047_2442 {
  condition:
    auto_rule_20250726224042_8529 or auto_rule_20250726224045_5119
}