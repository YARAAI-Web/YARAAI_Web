rule auto_rule_20250726113739_9008 {
  strings:
    $o0 = "dword_40B36C" wide ascii nocase
    $o1 = "off_40B278" wide ascii nocase
    $o2 = "x54634DC4" wide ascii nocase
    $o3 = "dword_40B2A8" wide ascii nocase
  condition:
    4 of ($o*)
}