rule auto_rule_20250726172256_4783 {
  strings:
    $o0 = "dword_412254" wide ascii nocase
    $o1 = "TrailDown0_0" wide ascii nocase
    $o2 = "TargetIp" wide ascii nocase
    $o3 = "_wincmdln" wide ascii nocase
  condition:
    4 of ($o*)
}