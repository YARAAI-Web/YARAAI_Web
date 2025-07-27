rule auto_rule_20250726173002_4286 {
  strings:
    $o0 = "word_4C10B4" wide ascii nocase
    $o1 = "AutoIt" wide ascii nocase
    $o2 = "dword_4C15F4" wide ascii nocase
  condition:
    3 of ($o*)
}