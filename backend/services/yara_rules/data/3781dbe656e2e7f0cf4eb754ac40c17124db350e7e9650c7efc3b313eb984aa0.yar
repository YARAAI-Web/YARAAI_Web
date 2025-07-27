rule auto_rule_20250726105314_9376 {
  strings:
    $o0 = "EventA" wide ascii nocase
    $o1 = "x5D8u" wide ascii nocase
    $o2 = "off_435DD2" wide ascii nocase
    $o3 = "dword_435DBE" wide ascii nocase
    $o4 = "dwActiveProcessorMask" wide ascii nocase
  condition:
    4 of ($o*)
}