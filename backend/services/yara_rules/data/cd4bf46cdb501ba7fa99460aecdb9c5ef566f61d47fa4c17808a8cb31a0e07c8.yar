rule auto_rule_20250727041617_2364 {
  strings:
    $o0 = "x7336000010FFLL" wide ascii nocase
    $o1 = "xAF2B8DF8" wide ascii nocase
    $o2 = "qword_40A5F4" wide ascii nocase
    $o3 = "word_40A790" wide ascii nocase
    $o4 = "x71A5" wide ascii nocase
  condition:
    4 of ($o*)
}