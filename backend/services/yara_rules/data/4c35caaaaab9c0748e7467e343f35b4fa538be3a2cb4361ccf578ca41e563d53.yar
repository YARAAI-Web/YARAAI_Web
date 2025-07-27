rule auto_rule_20250726143705_0029 {
  strings:
    $o0 = "_NLG_Notify1" wide ascii nocase
    $o1 = "UnwindUp0_0" wide ascii nocase
    $o2 = "dword_44A3B4" wide ascii nocase
  condition:
    3 of ($o*)
}