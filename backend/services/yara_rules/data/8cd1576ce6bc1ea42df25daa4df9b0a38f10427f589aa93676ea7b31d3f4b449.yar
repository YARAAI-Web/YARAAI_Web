rule auto_rule_20250726172751_7780 {
  strings:
    $o0 = "byte_44F1B8" wide ascii nocase
    $o1 = "dword_45D8AC" wide ascii nocase
    $o2 = "_NLG_Notify1" wide ascii nocase
  condition:
    3 of ($o*)
}