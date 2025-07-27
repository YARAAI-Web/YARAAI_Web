rule auto_rule_20250726170117_8362 {
  strings:
    $o0 = "pArpEntry" wide ascii nocase
    $o1 = "lpszValueName" wide ascii nocase
    $o2 = "lpwsTransportName" wide ascii nocase
  condition:
    3 of ($o*)
}