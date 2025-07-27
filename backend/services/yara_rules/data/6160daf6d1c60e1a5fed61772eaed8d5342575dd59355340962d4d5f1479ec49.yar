rule auto_rule_20250727040420_8366 {
  strings:
    $o0 = "PoolWithTagPriority" wide ascii nocase
    $o1 = "word_1E99A" wide ascii nocase
    $o2 = "aHidiaiet" wide ascii nocase
  condition:
    3 of ($o*)
}