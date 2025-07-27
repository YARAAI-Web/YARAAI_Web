rule auto_rule_20250726120159_5095 {
  strings:
    $o0 = "RtlCompareUnicodeString" wide ascii nocase
    $o1 = "__readcr0" wide ascii nocase
    $o2 = "asc_1ECB2" wide ascii nocase
  condition:
    3 of ($o*)
}