rule auto_rule_20250727001052_5761 {
  strings:
    $o0 = "TSPI_providerUIIdentify" wide ascii nocase
    $o1 = "TSPI_lineGetAddressStatus" wide ascii nocase
    $o2 = "dwInitialSize" wide ascii nocase
  condition:
    3 of ($o*)
}