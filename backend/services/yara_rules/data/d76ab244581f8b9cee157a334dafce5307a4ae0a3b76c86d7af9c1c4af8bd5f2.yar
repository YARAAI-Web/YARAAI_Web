rule auto_rule_20250726203557_9850 {
  strings:
    $o0 = "dword_78ABC" wide ascii nocase
    $o1 = "dword_77F54" wide ascii nocase
    $o2 = "word_1EC5E" wide ascii nocase
  condition:
    3 of ($o*)
}