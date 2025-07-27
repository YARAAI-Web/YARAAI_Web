rule auto_rule_20250726210431_2524 {
  strings:
    $o0 = "dword_78408" wide ascii nocase
    $o1 = "word_1E782" wide ascii nocase
    $o2 = "dword_78394" wide ascii nocase
    $o3 = "init" wide ascii nocase
  condition:
    4 of ($o*)
}