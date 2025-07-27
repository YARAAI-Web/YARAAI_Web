rule auto_rule_20250726231544_0133 {
  strings:
    $o0 = "dword_4643D4" wide ascii nocase
    $o1 = "dword_463ADC" wide ascii nocase
  condition:
    all of them
}