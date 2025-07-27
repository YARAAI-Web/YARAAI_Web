rule auto_rule_20250726161544_9871 {
  strings:
    $o0 = "x13FC" wide ascii nocase
    $o1 = "dword_40A670" wide ascii nocase
    $o2 = "x2FE" wide ascii nocase
    $o3 = "x6699u" wide ascii nocase
    $o4 = "x22BA" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726161546_8393 {
  strings:
    $o0 = "dword_40A66C" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726161549_1612 {
  condition:
    auto_rule_20250726161544_9871 or auto_rule_20250726161546_8393
}