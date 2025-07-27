rule auto_rule_20250726120309_4637 {
  strings:
    $o0 = "word_1E82A" wide ascii nocase
    $o1 = "dword_78144" wide ascii nocase
    $o2 = "dword_7817C" wide ascii nocase
    $o3 = "init" wide ascii nocase
  condition:
    4 of ($o*)
}