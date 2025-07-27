rule auto_rule_20250726121838_7520 {
  strings:
    $o0 = "VirtualFree" wide ascii nocase
    $o1 = "dword_475678" wide ascii nocase
    $o2 = "off_4751F0" wide ascii nocase
  condition:
    3 of ($o*)
}