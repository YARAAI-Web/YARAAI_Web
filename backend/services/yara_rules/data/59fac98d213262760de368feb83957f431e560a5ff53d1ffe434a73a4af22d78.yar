rule auto_rule_20250726170541_8504 {
  strings:
    $o0 = "x3D1u" wide ascii nocase
    $o1 = "TargetIp" wide ascii nocase
    $o2 = "x41C4u" wide ascii nocase
    $o3 = "CodePagea" wide ascii nocase
  condition:
    4 of ($o*)
}