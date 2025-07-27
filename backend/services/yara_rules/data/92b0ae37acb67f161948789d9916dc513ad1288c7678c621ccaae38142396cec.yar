rule auto_rule_20250726100312_5060 {
  strings:
    $o0 = "xFFBFF9F9" wide ascii nocase
    $o1 = "off_41E761" wide ascii nocase
    $o2 = "dword_452305" wide ascii nocase
    $o3 = "dword_41E849" wide ascii nocase
    $o4 = "dword_451030" wide ascii nocase
  condition:
    4 of ($o*)
}