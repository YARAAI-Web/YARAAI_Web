rule auto_rule_20250727042113_5681 {
  strings:
    $o0 = "dword_411D74" wide ascii nocase
    $o1 = "_wincmdln" wide ascii nocase
    $o2 = "dword_411D7C" wide ascii nocase
  condition:
    3 of ($o*)
}