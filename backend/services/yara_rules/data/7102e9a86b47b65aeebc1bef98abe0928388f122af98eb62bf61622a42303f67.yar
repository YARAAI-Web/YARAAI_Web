rule auto_rule_20250726084158_7451 {
  strings:
    $o0 = "off_1400053D8" wide ascii nocase
    $o1 = "aAvbn" wide ascii nocase
    $o2 = "lstrlenA" wide ascii nocase
  condition:
    3 of ($o*)
}