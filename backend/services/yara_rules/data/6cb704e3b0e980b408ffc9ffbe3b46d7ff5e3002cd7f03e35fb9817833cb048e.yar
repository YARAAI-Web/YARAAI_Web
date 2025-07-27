rule auto_rule_20250726220507_3361 {
  strings:
    $o0 = "UnwindUp1_0" wide ascii nocase
    $o1 = "lpCharType" wide ascii nocase
    $o2 = "main_loop_2" wide ascii nocase
    $o3 = "word_45D030" wide ascii nocase
  condition:
    4 of ($o*)
}