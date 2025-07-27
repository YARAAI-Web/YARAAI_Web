rule auto_rule_20250726131703_7286 {
  strings:
    $o0 = "off_4BA004" wide ascii nocase
    $o1 = "off_4BADB0" wide ascii nocase
    $o2 = "dword_4B6A2C" wide ascii nocase
    $o3 = "IsThemeActive" wide ascii nocase
    $o4 = "dbl_4BA060" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726131706_5896 {
  strings:
    $o0 = "word_492918" wide ascii nocase
    $o1 = "dword_4C10B0" wide ascii nocase
    $o2 = "not_in_range_0" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726131710_5038 {
  condition:
    auto_rule_20250726131703_7286 or auto_rule_20250726131706_5896
}