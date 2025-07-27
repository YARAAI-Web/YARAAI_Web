rule auto_rule_20250726114820_8767 {
  strings:
    $o0 = "dword_42A028" wide ascii nocase
    $o1 = "_NLG_Notify" wide ascii nocase
    $o2 = "TargetIp" wide ascii nocase
  condition:
    3 of ($o*)
}