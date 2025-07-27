rule auto_rule_20250726153012_7265 {
  strings:
    $o0 = "x400FF" wide ascii nocase
    $o1 = "__std_type_info_name" wide ascii nocase
    $o2 = "__castguard_check_failure_fastfail" wide ascii nocase
    $o3 = "xFEFFFFFF" wide ascii nocase
  condition:
    4 of ($o*)
}