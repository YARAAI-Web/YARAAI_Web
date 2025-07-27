rule auto_rule_20250726065602_6049 {
  strings:
    $o0 = "strcspn" wide ascii nocase
    $o1 = "_NLG_Notify" wide ascii nocase
    $o2 = "dword_46AA5C" wide ascii nocase
  condition:
    3 of ($o*)
}