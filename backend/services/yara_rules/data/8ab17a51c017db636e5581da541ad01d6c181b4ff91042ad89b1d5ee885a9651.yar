rule auto_rule_20250726220212_1481 {
  strings:
    $o0 = "x40B71D00" wide ascii nocase
    $o1 = "x495B4500" wide ascii nocase
    $o2 = "x78C80600" wide ascii nocase
    $o3 = "dword_43B40A" wide ascii nocase
    $o4 = "x61379" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726220215_8202 {
  strings:
    $o0 = "dword_43B67C" wide ascii nocase
    $o1 = "dword_43B0AB" wide ascii nocase
    $o2 = "dword_43B1E3" wide ascii nocase
    $o3 = "dword_43B5A2" wide ascii nocase
    $o4 = "dword_43B733" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726220218_1854 {
  strings:
    $o0 = "dword_43B473" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726220228_6939 {
  condition:
    (auto_rule_20250726220212_1481 and auto_rule_20250726220215_8202) or (auto_rule_20250726220212_1481 and auto_rule_20250726220218_1854) or (auto_rule_20250726220215_8202 and auto_rule_20250726220218_1854)
}