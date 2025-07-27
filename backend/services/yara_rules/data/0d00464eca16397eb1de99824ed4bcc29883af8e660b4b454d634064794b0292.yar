rule auto_rule_20250726112220_2245 {
  strings:
    $o0 = "dword_7F800" wide ascii nocase
    $o1 = "word_1DF32" wide ascii nocase
    $o2 = "dword_7F770" wide ascii nocase
  condition:
    3 of ($o*)
}