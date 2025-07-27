rule auto_rule_20250726211055_3646 {
  strings:
    $o0 = "off_51A5FC" wide ascii nocase
    $o1 = "off_51FB98" wide ascii nocase
    $o2 = ".minfo" wide ascii nocase
  condition:
    3 of ($o*)
}