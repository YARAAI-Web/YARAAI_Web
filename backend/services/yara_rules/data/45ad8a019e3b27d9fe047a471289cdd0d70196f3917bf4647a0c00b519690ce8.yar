rule auto_rule_20250726231604_2278 {
  strings:
    $o0 = "_NLG_Notify1" wide ascii nocase
    $o1 = "dword_448F24" wide ascii nocase
  condition:
    all of them
}