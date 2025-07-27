rule auto_rule_20250726094236_1443 {
  strings:
    $o0 = "off_46E760" wide ascii nocase
    $o1 = "byte_46EA54" wide ascii nocase
    $o2 = "dword_46E908" wide ascii nocase
    $o3 = "report_failure" wide ascii nocase
    $o4 = "off_46E000" wide ascii nocase
  condition:
    4 of ($o*)
}