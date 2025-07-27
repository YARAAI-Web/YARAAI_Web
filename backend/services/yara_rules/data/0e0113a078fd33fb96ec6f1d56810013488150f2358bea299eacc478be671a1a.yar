rule auto_rule_20250726120406_2161 {
  strings:
    $o0 = "strcspn" wide ascii nocase
    $o1 = "off_466ECC" wide ascii nocase
    $o2 = "__sbh_alloc_new_group" wide ascii nocase
    $o3 = "report_failure" wide ascii nocase
  condition:
    4 of ($o*)
}