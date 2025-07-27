rule auto_rule_20250726134052_3965 {
  strings:
    $o0 = "_cfltcvt" wide ascii nocase
    $o1 = "word_4189FA" wide ascii nocase
    $o2 = "_heap_init" wide ascii nocase
  condition:
    3 of ($o*)
}