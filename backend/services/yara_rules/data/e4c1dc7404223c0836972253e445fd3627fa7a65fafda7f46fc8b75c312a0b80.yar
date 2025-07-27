rule auto_rule_20250726183628_4600 {
  strings:
    $o0 = "x8FBuLL" wide ascii nocase
    $o1 = "ftCreationTime" wide ascii nocase
    $o2 = "x7AD" wide ascii nocase
    $o3 = "dword_4295EC" wide ascii nocase
    $o4 = "BB8h" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726183631_3465 {
  strings:
    $o0 = "dword_429959" wide ascii nocase
    $o1 = "x6807" wide ascii nocase
    $o2 = "xFFFFB7AD" wide ascii nocase
    $o3 = "off_429100" wide ascii nocase
    $o4 = "dword_429384" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726183635_2461 {
  strings:
    $o0 = "x73F7" wide ascii nocase
    $o1 = "dword_429504" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726183647_5138 {
  condition:
    (auto_rule_20250726183628_4600 and auto_rule_20250726183631_3465) or (auto_rule_20250726183628_4600 and auto_rule_20250726183635_2461) or (auto_rule_20250726183631_3465 and auto_rule_20250726183635_2461)
}