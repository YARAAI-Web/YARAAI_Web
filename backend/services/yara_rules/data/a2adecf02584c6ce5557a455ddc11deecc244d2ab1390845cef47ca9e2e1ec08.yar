rule auto_rule_20250726204519_0893 {
  strings:
    $o0 = "dword_4690A8" wide ascii nocase
    $o1 = "_NLG_Notify" wide ascii nocase
    $o2 = "UsedDefaultChar" wide ascii nocase
  condition:
    3 of ($o*)
}