rule auto_rule_20250726122052_7191 {
  strings:
    $o0 = "x8A85" wide ascii nocase
    $o1 = "dword_421B8C" wide ascii nocase
    $o2 = "dword_421C92" wide ascii nocase
    $o3 = "word_4239A2" wide ascii nocase
  condition:
    4 of ($o*)
}