rule auto_rule_20250726142518_2501 {
  strings:
    $o0 = "dwCreationDisposition" wide ascii nocase
    $o1 = "aGsyst12111cgcr" wide ascii nocase
    $o2 = "dword_42EEBC" wide ascii nocase
  condition:
    3 of ($o*)
}