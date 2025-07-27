rule auto_rule_20250726152932_0020 {
  strings:
    $o0 = "dword_788D8" wide ascii nocase
    $o1 = "word_1E8AE" wide ascii nocase
    $o2 = "wcscat" wide ascii nocase
    $o3 = "RtlCompareUnicodeString" wide ascii nocase
  condition:
    4 of ($o*)
}