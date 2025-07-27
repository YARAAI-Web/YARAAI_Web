rule auto_rule_20250726232833_4780 {
  strings:
    $o0 = "off_463998" wide ascii nocase
    $o1 = "nModule" wide ascii nocase
    $o2 = "start_byte_3" wide ascii nocase
  condition:
    3 of ($o*)
}