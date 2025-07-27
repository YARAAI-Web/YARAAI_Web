rule auto_rule_20250726064005_1127 {
  strings:
    $o0 = "CodePagea" wide ascii nocase
    $o1 = "dword_44C4F0" wide ascii nocase
    $o2 = "_NLG_Notify" wide ascii nocase
    $o3 = "dword_44B7D0" wide ascii nocase
  condition:
    4 of ($o*)
}