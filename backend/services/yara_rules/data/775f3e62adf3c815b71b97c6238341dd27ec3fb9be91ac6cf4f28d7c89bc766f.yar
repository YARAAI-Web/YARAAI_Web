rule auto_rule_20250726131818_4419 {
  strings:
    $o0 = "byte_40A07C" wide ascii nocase
  condition:
    all of them
}