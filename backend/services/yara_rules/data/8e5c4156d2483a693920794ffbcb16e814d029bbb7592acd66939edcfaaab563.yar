rule auto_rule_20250726180806_7976 {
  strings:
    $o0 = "off_40B718" wide ascii nocase
    $o1 = "dword_40B734" wide ascii nocase
    $o2 = "x7973u" wide ascii nocase
    $o3 = "x41A1u" wide ascii nocase
    $o4 = "kr28_8" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726180808_7898 {
  strings:
    $o0 = "dword_40B7B4" wide ascii nocase
    $o1 = "dword_40B738" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726180812_6930 {
  condition:
    auto_rule_20250726180806_7976 or auto_rule_20250726180808_7898
}