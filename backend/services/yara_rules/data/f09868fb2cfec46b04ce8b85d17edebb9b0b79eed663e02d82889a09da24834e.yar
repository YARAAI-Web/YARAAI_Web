rule auto_rule_20250726213826_6367 {
  strings:
    $o0 = "word_42E0B3" wide ascii nocase
    $o1 = "xC4B0" wide ascii nocase
    $o2 = "dwInfoType" wide ascii nocase
    $o3 = "xF89C85F4" wide ascii nocase
    $o4 = "dword_42D008" wide ascii nocase
  condition:
    4 of ($o*)
}