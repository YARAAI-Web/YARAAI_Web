rule auto_rule_20250726143349_5900 {
  strings:
    $o0 = "dword_42705C" wide ascii nocase
    $o1 = "_NLG_Notify1" wide ascii nocase
    $o2 = "dword_42722C" wide ascii nocase
  condition:
    3 of ($o*)
}