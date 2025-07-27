rule auto_rule_20250726095405_0307 {
  strings:
    $o0 = "dword_45CB08" wide ascii nocase
    $o1 = "word_42893A" wide ascii nocase
    $o2 = "dwInfoType" wide ascii nocase
  condition:
    3 of ($o*)
}