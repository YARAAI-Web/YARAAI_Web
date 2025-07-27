rule auto_rule_20250726110223_2262 {
  strings:
    $o0 = "dword_412230" wide ascii nocase
    $o1 = "dword_4118F4" wide ascii nocase
    $o2 = "_ctype" wide ascii nocase
  condition:
    3 of ($o*)
}