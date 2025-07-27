rule auto_rule_20250726225930_7353 {
  strings:
    $o0 = "Runtime" wide ascii nocase
    $o1 = "TargetIp" wide ascii nocase
    $o2 = "off_44D550" wide ascii nocase
    $o3 = "_c_exit" wide ascii nocase
  condition:
    4 of ($o*)
}