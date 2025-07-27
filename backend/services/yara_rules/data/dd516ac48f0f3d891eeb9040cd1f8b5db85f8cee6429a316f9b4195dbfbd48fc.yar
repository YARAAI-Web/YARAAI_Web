rule auto_rule_20250726063159_9105 {
  strings:
    $o0 = "dword_781C8" wide ascii nocase
    $o1 = "dword_1E704" wide ascii nocase
    $o2 = "kr00_2" wide ascii nocase
    $o3 = "init" wide ascii nocase
  condition:
    4 of ($o*)
}