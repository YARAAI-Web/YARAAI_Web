rule auto_rule_20250726074128_8728 {
  strings:
    $o0 = "off_402004" wide ascii nocase
    $o1 = "VirtualAllocEx" wide ascii nocase
  condition:
    all of them
}