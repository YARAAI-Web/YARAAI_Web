rule auto_rule_20250726201541_0528 {
  strings:
    $o0 = "TargetIp" wide ascii nocase
    $o1 = "off_4657BC" wide ascii nocase
    $o2 = "_nh_malloc" wide ascii nocase
    $o3 = "word_42898A" wide ascii nocase
  condition:
    4 of ($o*)
}