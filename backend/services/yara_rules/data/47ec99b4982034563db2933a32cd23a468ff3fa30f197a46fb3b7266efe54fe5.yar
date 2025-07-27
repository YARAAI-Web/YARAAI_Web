rule auto_rule_20250726204735_1790 {
  strings:
    $o0 = "word_44C690" wide ascii nocase
    $o1 = "dword_449020" wide ascii nocase
    $o2 = "dword_44C8EC" wide ascii nocase
  condition:
    3 of ($o*)
}