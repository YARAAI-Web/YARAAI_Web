rule auto_rule_20250727011246_7306 {
  strings:
    $o0 = "word_1EA52" wide ascii nocase
    $o1 = "dword_1E80C" wide ascii nocase
    $o2 = "dword_7EB74" wide ascii nocase
    $o3 = "init" wide ascii nocase
  condition:
    4 of ($o*)
}