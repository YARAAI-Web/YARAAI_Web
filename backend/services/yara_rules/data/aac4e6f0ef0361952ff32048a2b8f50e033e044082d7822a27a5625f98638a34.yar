rule auto_rule_20250726150137_0908 {
  strings:
    $o0 = "UnwindUp3_0" wide ascii nocase
    $o1 = "dword_45FE64" wide ascii nocase
    $o2 = "dword_45FCF8" wide ascii nocase
    $o3 = "TargetIp" wide ascii nocase
  condition:
    4 of ($o*)
}