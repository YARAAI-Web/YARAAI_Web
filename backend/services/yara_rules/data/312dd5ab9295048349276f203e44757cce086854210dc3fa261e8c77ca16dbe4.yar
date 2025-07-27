rule auto_rule_20250726082433_6141 {
  strings:
    $o0 = "GetDriveTypeA" wide ascii nocase
    $o1 = "SnmpTfxClose" wide ascii nocase
  condition:
    all of them
}