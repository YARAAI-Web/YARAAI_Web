rule auto_rule_20250726164758_0645 {
  strings:
    $o0 = "off_40E528" wide ascii nocase
    $o1 = "dword_40E95C" wide ascii nocase
    $o2 = "_cftoa_l" wide ascii nocase
  condition:
    3 of ($o*)
}