rule auto_rule_20250726200321_2450 {
  strings:
    $o0 = "dword_449EAC" wide ascii nocase
    $o1 = "_NLG_Notify1" wide ascii nocase
    $o2 = "TargetIp" wide ascii nocase
  condition:
    3 of ($o*)
}