rule auto_rule_20250726124534_8189 {
  strings:
    $o0 = "x2868u" wide ascii nocase
    $o1 = "dword_426E81" wide ascii nocase
    $o2 = "dword_426EE1" wide ascii nocase
    $o3 = "xFFCD8D06" wide ascii nocase
  condition:
    4 of ($o*)
}