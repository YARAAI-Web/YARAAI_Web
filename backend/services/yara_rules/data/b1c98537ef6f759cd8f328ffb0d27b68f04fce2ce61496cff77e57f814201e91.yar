rule auto_rule_20250726221330_8888 {
  strings:
    $o0 = "word_40310C" wide ascii nocase
    $o1 = "dword_403004" wide ascii nocase
    $o2 = "dword_401050" wide ascii nocase
  condition:
    3 of ($o*)
}