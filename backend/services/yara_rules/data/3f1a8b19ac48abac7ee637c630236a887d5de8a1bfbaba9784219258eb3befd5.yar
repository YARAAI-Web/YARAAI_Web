rule auto_rule_20250726101835_6108 {
  strings:
    $o0 = "VirtualFree" wide ascii nocase
    $o1 = "off_410500" wide ascii nocase
    $o2 = "dword_410AE0" wide ascii nocase
  condition:
    3 of ($o*)
}