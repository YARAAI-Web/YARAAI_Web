rule auto_rule_20250727020602_8034 {
  strings:
    $o0 = "off_462ADC" wide ascii nocase
    $o1 = "terminated" wide ascii nocase
    $o2 = "dword_463454" wide ascii nocase
  condition:
    3 of ($o*)
}