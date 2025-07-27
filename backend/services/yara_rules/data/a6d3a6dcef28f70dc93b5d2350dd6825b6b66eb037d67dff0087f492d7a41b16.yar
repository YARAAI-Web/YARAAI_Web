rule auto_rule_20250726151005_4602 {
  strings:
    $o0 = "word_4C0B08" wide ascii nocase
    $o1 = "not_in_range" wide ascii nocase
    $o2 = "dword_4BB47C" wide ascii nocase
    $o3 = "fptan" wide ascii nocase
  condition:
    4 of ($o*)
}