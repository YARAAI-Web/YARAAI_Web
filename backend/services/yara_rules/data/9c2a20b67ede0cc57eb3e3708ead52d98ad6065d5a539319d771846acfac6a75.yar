rule auto_rule_20250726193359_3633 {
  strings:
    $o0 = "nConnecting" wide ascii nocase
    $o1 = "off_431950" wide ascii nocase
  condition:
    all of them
}