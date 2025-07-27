rule auto_rule_20250726214903_5782 {
  strings:
    $o0 = "word_4C0B08" wide ascii nocase
    $o1 = "exit_2" wide ascii nocase
    $o2 = "dword_4C10EC" wide ascii nocase
    $o3 = "IsThemeActive" wide ascii nocase
    $o4 = "off_4BA004" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726214907_4827 {
  strings:
    $o0 = "x7FF00000" wide ascii nocase
    $o1 = "negative_x_0" wide ascii nocase
    $o2 = "start_3" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726214908_5617 {
  condition:
    auto_rule_20250726214903_5782 or auto_rule_20250726214907_4827
}