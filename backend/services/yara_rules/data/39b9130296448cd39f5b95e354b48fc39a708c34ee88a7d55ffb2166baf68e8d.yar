rule auto_rule_20250727021812_4289 {
  strings:
    $o0 = "_NLG_Notify1" wide ascii nocase
    $o1 = "dword_40E020" wide ascii nocase
  condition:
    all of them
}