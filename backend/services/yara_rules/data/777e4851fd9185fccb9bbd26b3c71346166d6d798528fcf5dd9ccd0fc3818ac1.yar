rule auto_rule_20250726105232_9077 {
  strings:
    $o0 = "off_4653E8" wide ascii nocase
    $o1 = "pSid1" wide ascii nocase
  condition:
    all of them
}