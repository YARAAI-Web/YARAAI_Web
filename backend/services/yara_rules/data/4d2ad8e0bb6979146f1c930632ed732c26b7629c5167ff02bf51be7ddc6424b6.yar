rule auto_rule_20250726210338_8939 {
  strings:
    $o0 = "init" wide ascii nocase
    $o1 = "dword_77728" wide ascii nocase
    $o2 = "dword_78390" wide ascii nocase
    $o3 = "dword_78484" wide ascii nocase
    $o4 = "word_1E502" wide ascii nocase
  condition:
    4 of ($o*)
}