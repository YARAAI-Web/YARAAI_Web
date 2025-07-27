rule auto_rule_20250726225700_8728 {
  strings:
    $o0 = "dword_7842C" wide ascii nocase
    $o1 = "stru_78430" wide ascii nocase
    $o2 = "dword_783C8" wide ascii nocase
    $o3 = "dword_78120" wide ascii nocase
    $o4 = "init" wide ascii nocase
  condition:
    4 of ($o*)
}