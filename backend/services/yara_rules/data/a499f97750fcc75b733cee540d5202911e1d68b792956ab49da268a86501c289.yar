rule auto_rule_20250726122204_8843 {
  strings:
    $o0 = "word_40A794" wide ascii nocase
    $o1 = "dword_41011B" wide ascii nocase
    $o2 = "dword_40A56C" wide ascii nocase
    $o3 = "x10E930000A91BLL" wide ascii nocase
  condition:
    4 of ($o*)
}