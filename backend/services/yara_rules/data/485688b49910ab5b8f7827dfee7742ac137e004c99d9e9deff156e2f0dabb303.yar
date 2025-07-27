rule auto_rule_20250726142612_4945 {
  strings:
    $o0 = "dword_78334" wide ascii nocase
    $o1 = "word_1E992" wide ascii nocase
    $o2 = "init" wide ascii nocase
  condition:
    3 of ($o*)
}