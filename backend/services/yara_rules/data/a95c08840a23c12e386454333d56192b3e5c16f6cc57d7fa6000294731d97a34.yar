rule auto_rule_20250726132913_6547 {
  strings:
    $o0 = "stru_77558" wide ascii nocase
    $o1 = "dword_78290" wide ascii nocase
    $o2 = "dword_78284" wide ascii nocase
  condition:
    3 of ($o*)
}