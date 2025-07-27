rule auto_rule_20250727020728_7540 {
  strings:
    $o0 = "x22C088" wide ascii nocase
    $o1 = "word_1E572" wide ascii nocase
    $o2 = "dword_78164" wide ascii nocase
    $o3 = "dword_78454" wide ascii nocase
  condition:
    4 of ($o*)
}