rule auto_rule_20250726235911_7114 {
  strings:
    $o0 = "x18000" wide ascii nocase
    $o1 = "dword_47F390" wide ascii nocase
    $o2 = "x1FFE0" wide ascii nocase
    $o3 = "program" wide ascii nocase
  condition:
    4 of ($o*)
}