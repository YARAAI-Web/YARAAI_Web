rule auto_rule_20250727010340_2025 {
  strings:
    $o0 = "_NLG_Notify1" wide ascii nocase
    $o1 = "dword_4643D8" wide ascii nocase
    $o2 = "pHead" wide ascii nocase
  condition:
    3 of ($o*)
}