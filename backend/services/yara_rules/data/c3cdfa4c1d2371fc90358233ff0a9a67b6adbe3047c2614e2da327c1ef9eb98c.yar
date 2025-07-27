rule auto_rule_20250726133217_4560 {
  strings:
    $o0 = "word_42266E" wide ascii nocase
    $o1 = "dword_428559" wide ascii nocase
    $o2 = "dword_4284B9" wide ascii nocase
  condition:
    3 of ($o*)
}