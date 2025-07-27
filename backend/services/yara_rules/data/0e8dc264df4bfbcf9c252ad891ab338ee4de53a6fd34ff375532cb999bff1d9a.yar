rule auto_rule_20250726205856_7546 {
  strings:
    $o0 = "dword_401BD0" wide ascii nocase
    $o1 = "dword_402718" wide ascii nocase
    $o2 = "x314u" wide ascii nocase
    $o3 = "word_409624" wide ascii nocase
  condition:
    4 of ($o*)
}