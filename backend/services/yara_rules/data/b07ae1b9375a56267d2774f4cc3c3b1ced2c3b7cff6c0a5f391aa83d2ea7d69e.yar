rule auto_rule_20250726063259_0887 {
  strings:
    $o0 = "x5A05u" wide ascii nocase
    $o1 = "x6E2" wide ascii nocase
    $o2 = "x30D0u" wide ascii nocase
    $o3 = "xFFFFACD7" wide ascii nocase
    $o4 = "dword_4295D8" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726063303_1612 {
  strings:
    $o0 = "dword_429708" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726063308_1535 {
  condition:
    auto_rule_20250726063259_0887 or auto_rule_20250726063303_1612
}