rule auto_rule_20250726202852_3089 {
  strings:
    $o0 = "vtable" wide ascii nocase
    $o1 = "v277" wide ascii nocase
    $o2 = "off_1400BA400" wide ascii nocase
    $o3 = "off_1400BA800" wide ascii nocase
  condition:
    4 of ($o*)
}