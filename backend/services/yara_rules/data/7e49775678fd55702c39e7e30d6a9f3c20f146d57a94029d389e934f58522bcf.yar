rule auto_rule_20250726062627_8834 {
  strings:
    $o0 = "dword_46443C" wide ascii nocase
    $o1 = "lpCharType" wide ascii nocase
    $o2 = "xC0000092" wide ascii nocase
    $o3 = "dword_463AD8" wide ascii nocase
    $o4 = "off_463C44" wide ascii nocase
  condition:
    4 of ($o*)
}