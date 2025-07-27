rule auto_rule_20250726183844_3452 {
  strings:
    $o0 = "dword_45CAF4" wide ascii nocase
    $o1 = "dword_42A028" wide ascii nocase
    $o2 = "off_45C90C" wide ascii nocase
  condition:
    3 of ($o*)
}