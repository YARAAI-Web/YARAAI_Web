rule auto_rule_20250726191445_9676 {
  strings:
    $o0 = "word_1E502" wide ascii nocase
    $o1 = "Executive" wide ascii nocase
    $o2 = "xFFFEFFFF" wide ascii nocase
  condition:
    3 of ($o*)
}