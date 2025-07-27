rule auto_rule_20250726094449_6566 {
  strings:
    $o0 = "fill_with_EOS_dwords" wide ascii nocase
    $o1 = "dword_456BB8" wide ascii nocase
    $o2 = "off_455CFC" wide ascii nocase
    $o3 = "report_failure" wide ascii nocase
    $o4 = "dword_456B9C" wide ascii nocase
  condition:
    4 of ($o*)
}