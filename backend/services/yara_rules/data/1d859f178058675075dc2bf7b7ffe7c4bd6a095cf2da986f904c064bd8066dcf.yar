rule auto_rule_20250726183701_3062 {
  strings:
    $o0 = "off_45FD80" wide ascii nocase
    $o1 = "byte_446AD8" wide ascii nocase
    $o2 = "x402560" wide ascii nocase
    $o3 = "memcpy_0" wide ascii nocase
  condition:
    4 of ($o*)
}