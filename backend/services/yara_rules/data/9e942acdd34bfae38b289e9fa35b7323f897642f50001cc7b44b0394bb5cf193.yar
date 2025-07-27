rule auto_rule_20250727040631_3829 {
  strings:
    $o0 = "dword_1E6EC" wide ascii nocase
    $o1 = "word_1DEF2" wide ascii nocase
    $o2 = "dword_1E694" wide ascii nocase
  condition:
    3 of ($o*)
}