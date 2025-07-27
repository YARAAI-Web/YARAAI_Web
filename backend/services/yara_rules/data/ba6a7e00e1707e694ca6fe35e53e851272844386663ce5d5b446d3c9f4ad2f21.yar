rule auto_rule_20250726195018_4150 {
  strings:
    $o0 = "x4817" wide ascii nocase
    $o1 = "x1AA0u" wide ascii nocase
    $o2 = "szCurrent" wide ascii nocase
    $o3 = "CreatePalette" wide ascii nocase
    $o4 = "xF89C8531" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726195021_7884 {
  strings:
    $o0 = "x21FD" wide ascii nocase
    $o1 = "x2141" wide ascii nocase
    $o2 = "x8706" wide ascii nocase
    $o3 = "x5F13u" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726195027_6868 {
  condition:
    auto_rule_20250726195018_4150 or auto_rule_20250726195021_7884
}