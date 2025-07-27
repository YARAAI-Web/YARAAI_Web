rule auto_rule_20250726221056_3553 {
  strings:
    $o0 = "off_402004" wide ascii nocase
    $o1 = "VirtualAllocEx" wide ascii nocase
    $o2 = "aStftware" wide ascii nocase
  condition:
    3 of ($o*)
}