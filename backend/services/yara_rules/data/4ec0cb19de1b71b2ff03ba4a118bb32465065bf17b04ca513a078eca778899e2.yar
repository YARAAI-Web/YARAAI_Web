rule auto_rule_20250727015144_9850 {
  strings:
    $o0 = "SnmpTfxClose" wide ascii nocase
  condition:
    all of them
}