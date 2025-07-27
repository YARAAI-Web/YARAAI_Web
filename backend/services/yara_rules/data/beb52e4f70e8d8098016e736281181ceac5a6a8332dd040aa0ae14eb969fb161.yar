rule auto_rule_20250726220518_7449 {
  strings:
    $o0 = "off_469678" wide ascii nocase
    $o1 = "lpCharType" wide ascii nocase
    $o2 = "dword_4699E0" wide ascii nocase
    $o3 = "dword_469284" wide ascii nocase
  condition:
    4 of ($o*)
}