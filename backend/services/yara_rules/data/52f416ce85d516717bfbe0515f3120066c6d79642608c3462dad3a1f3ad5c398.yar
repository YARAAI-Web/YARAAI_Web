rule auto_rule_20250726234249_3898 {
  strings:
    $o0 = "dword_456C10" wide ascii nocase
    $o1 = "GetWsChanges" wide ascii nocase
    $o2 = "_RoundMan" wide ascii nocase
    $o3 = "overrun" wide ascii nocase
  condition:
    4 of ($o*)
}