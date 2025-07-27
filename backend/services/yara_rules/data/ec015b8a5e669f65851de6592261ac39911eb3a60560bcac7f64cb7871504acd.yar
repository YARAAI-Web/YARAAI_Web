rule auto_rule_20250726214108_0312 {
  strings:
    $o0 = "byte_443A58" wide ascii nocase
    $o1 = "dword_45CEEC" wide ascii nocase
    $o2 = "dword_45C314" wide ascii nocase
    $o3 = "fill_dwords_with_EOS" wide ascii nocase
    $o4 = "dword_45C2DC" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726214111_4792 {
  strings:
    $o0 = "_cpinfo" wide ascii nocase
    $o1 = "dword_45CAF4" wide ascii nocase
    $o2 = "dword_42A020" wide ascii nocase
    $o3 = "__crtInitCritSecNoSpinCount" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726214115_2546 {
  condition:
    auto_rule_20250726214108_0312 or auto_rule_20250726214111_4792
}