rule auto_rule_20250726161111_7715 {
  strings:
    $o0 = "dword_466008" wide ascii nocase
    $o1 = "dword_4664AC" wide ascii nocase
    $o2 = "off_465B34" wide ascii nocase
    $o3 = "dword_465FC8" wide ascii nocase
  condition:
    4 of ($o*)
}