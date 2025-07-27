rule auto_rule_20250726210830_0567 {
  strings:
    $o0 = "dword_426EB1" wide ascii nocase
    $o1 = "xFFCD8D06" wide ascii nocase
    $o2 = "dword_426E8D" wide ascii nocase
    $o3 = "off_426141" wide ascii nocase
    $o4 = "dword_426EC9" wide ascii nocase
  condition:
    4 of ($o*)
}