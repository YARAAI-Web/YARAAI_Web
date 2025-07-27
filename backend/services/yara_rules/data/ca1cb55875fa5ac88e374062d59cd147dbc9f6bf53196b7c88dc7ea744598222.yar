rule auto_rule_20250726160823_6437 {
  strings:
    $o0 = "word_418A42" wide ascii nocase
    $o1 = "GdipFree" wide ascii nocase
    $o2 = "_mtdeletelocks" wide ascii nocase
    $o3 = "dword_456CC8" wide ascii nocase
  condition:
    4 of ($o*)
}