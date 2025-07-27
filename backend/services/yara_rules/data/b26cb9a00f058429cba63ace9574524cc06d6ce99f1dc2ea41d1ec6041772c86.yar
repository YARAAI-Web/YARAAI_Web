rule auto_rule_20250726233945_2873 {
  strings:
    $o0 = "byte_44F1B8" wide ascii nocase
    $o1 = "gu_return" wide ascii nocase
    $o2 = "dword_45D3CC" wide ascii nocase
  condition:
    3 of ($o*)
}