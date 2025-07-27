rule auto_rule_20250726081755_7708 {
  strings:
    $o0 = "xFFCD8D0A" wide ascii nocase
    $o1 = "dword_432433" wide ascii nocase
    $o2 = "nAtom" wide ascii nocase
  condition:
    3 of ($o*)
}