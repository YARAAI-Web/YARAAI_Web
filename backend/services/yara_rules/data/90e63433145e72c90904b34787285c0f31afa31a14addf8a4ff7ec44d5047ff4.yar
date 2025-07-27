rule auto_rule_20250726193216_4920 {
  strings:
    $o0 = "dword_46A0B0" wide ascii nocase
    $o1 = "dword_469D58" wide ascii nocase
    $o2 = "word_4698EC" wide ascii nocase
    $o3 = "SrcSizeInBytes" wide ascii nocase
  condition:
    4 of ($o*)
}