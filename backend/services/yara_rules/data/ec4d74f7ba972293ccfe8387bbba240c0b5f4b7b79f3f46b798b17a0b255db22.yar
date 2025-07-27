rule auto_rule_20250726160800_3209 {
  strings:
    $o0 = "dword_1400DB520" wide ascii nocase
    $o1 = "dword_1400DB670" wide ascii nocase
    $o2 = "dword_1400DB954" wide ascii nocase
  condition:
    3 of ($o*)
}