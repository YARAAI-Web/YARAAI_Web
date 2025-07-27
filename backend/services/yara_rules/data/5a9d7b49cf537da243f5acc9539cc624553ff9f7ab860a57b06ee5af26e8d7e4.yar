rule auto_rule_20250726114317_2924 {
  strings:
    $o0 = "VirtualAddresses" wide ascii nocase
    $o1 = "EnumPropsExW" wide ascii nocase
    $o2 = "x14B00u" wide ascii nocase
    $o3 = "CancelIo" wide ascii nocase
  condition:
    4 of ($o*)
}