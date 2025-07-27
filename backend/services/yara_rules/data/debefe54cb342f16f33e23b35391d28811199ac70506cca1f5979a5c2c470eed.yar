rule auto_rule_20250726142956_2248 {
  strings:
    $o0 = "dword_40ABC8" wide ascii nocase
    $o1 = "_calloc_impl" wide ascii nocase
    $o2 = "word_40B5D0" wide ascii nocase
    $o3 = "word_40B5CC" wide ascii nocase
  condition:
    4 of ($o*)
}