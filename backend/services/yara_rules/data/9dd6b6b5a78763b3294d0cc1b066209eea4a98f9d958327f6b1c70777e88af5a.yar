rule auto_rule_20250726060836_5155 {
  strings:
    $o0 = "cchMaxCount" wide ascii nocase
    $o1 = "SetCommState" wide ascii nocase
    $o2 = "lpStartAddress" wide ascii nocase
    $o3 = "lpProcessInformation" wide ascii nocase
    $o4 = "lpTotalNumberOfClusters" wide ascii nocase
  condition:
    4 of ($o*)
}