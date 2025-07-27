rule auto_rule_20250726125134_1113 {
  strings:
    $o0 = "dword_40A63C" wide ascii nocase
    $o1 = "x566D" wide ascii nocase
    $o2 = "dword_40A508" wide ascii nocase
    $o3 = "x6978" wide ascii nocase
    $o4 = "word_40A794" wide ascii nocase
  condition:
    4 of ($o*)
}