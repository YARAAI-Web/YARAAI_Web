rule auto_rule_20250726121722_0987 {
  strings:
    $o0 = "algn_45D032" wide ascii nocase
    $o1 = "_except_handler3" wide ascii nocase
    $o2 = "word_45D030" wide ascii nocase
  condition:
    3 of ($o*)
}