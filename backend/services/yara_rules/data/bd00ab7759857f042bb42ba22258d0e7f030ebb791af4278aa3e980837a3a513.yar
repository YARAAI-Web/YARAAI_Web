rule auto_rule_20250727001930_1273 {
  strings:
    $o0 = "sysenter" wide ascii nocase
    $o1 = "off_469B88" wide ascii nocase
  condition:
    all of them
}