rule auto_rule_20250726171701_3560 {
  strings:
    $o0 = "word_460110" wide ascii nocase
    $o1 = "main_loop_2" wide ascii nocase
    $o2 = "dword_45FFEC" wide ascii nocase
  condition:
    3 of ($o*)
}