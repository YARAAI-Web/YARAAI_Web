rule auto_rule_20250726082737_6798 {
  strings:
    $o0 = "dword_449E24" wide ascii nocase
    $o1 = "dword_449E2C" wide ascii nocase
  condition:
    all of them
}