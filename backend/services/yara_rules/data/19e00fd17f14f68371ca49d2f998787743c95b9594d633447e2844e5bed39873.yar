rule auto_rule_20250726223912_1637 {
  strings:
    $o0 = "CryptExportKey" wide ascii nocase
    $o1 = "ppsEditable" wide ascii nocase
    $o2 = "byte_419F40" wide ascii nocase
  condition:
    3 of ($o*)
}