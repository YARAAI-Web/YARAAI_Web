rule auto_rule_20250726152144_2230 {
  strings:
    $o0 = "dword_4343AF" wide ascii nocase
    $o1 = "dword_431018" wide ascii nocase
    $o2 = "dword_42F014" wide ascii nocase
  condition:
    3 of ($o*)
}