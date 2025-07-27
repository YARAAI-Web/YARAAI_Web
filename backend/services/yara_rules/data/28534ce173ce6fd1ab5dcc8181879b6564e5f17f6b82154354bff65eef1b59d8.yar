rule auto_rule_20250726155256_6102 {
  strings:
    $o0 = "_Locinfo_ctor" wide ascii nocase
    $o1 = "word_14006BC2E" wide ascii nocase
    $o2 = "dword_140075634" wide ascii nocase
    $o3 = "dword_140075714" wide ascii nocase
  condition:
    4 of ($o*)
}