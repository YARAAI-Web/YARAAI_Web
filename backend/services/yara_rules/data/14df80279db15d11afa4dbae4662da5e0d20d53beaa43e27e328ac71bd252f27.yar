rule auto_rule_20250727023812_4961 {
  strings:
    $o0 = "flAllocationType" wide ascii nocase
    $o1 = "OpenWindowStationA" wide ascii nocase
    $o2 = "nFilterType" wide ascii nocase
  condition:
    3 of ($o*)
}