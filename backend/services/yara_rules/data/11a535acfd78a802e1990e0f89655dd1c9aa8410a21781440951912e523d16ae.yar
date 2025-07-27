rule auto_rule_20250726063536_4272 {
  strings:
    $o0 = "dword_45B12C" wide ascii nocase
    $o1 = "SrcSizeInBytes" wide ascii nocase
    $o2 = "_ioinit" wide ascii nocase
  condition:
    3 of ($o*)
}