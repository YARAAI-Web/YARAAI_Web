rule auto_rule_20250726174840_9005 {
  strings:
    $o0 = "dword_429574" wide ascii nocase
    $o1 = "x2F3FEA51F993LL" wide ascii nocase
    $o2 = "dword_4298B9" wide ascii nocase
    $o3 = "x5EC7" wide ascii nocase
    $o4 = "x1CFD" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726174842_1198 {
  strings:
    $o0 = "xB23B8F09EDAAD89CuLL" wide ascii nocase
    $o1 = "xFF5F" wide ascii nocase
    $o2 = "x7672u" wide ascii nocase
    $o3 = "x3FC8" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726174846_0960 {
  condition:
    auto_rule_20250726174840_9005 or auto_rule_20250726174842_1198
}