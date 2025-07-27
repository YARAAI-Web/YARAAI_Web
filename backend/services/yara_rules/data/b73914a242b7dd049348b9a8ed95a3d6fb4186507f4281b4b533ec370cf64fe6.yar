rule auto_rule_20250726071540_4930 {
  strings:
    $o0 = "dword_45BF84" wide ascii nocase
    $o1 = "dword_45AF64" wide ascii nocase
    $o2 = "dword_45ABCC" wide ascii nocase
  condition:
    3 of ($o*)
}