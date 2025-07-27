rule auto_rule_20250726095103_4128 {
  strings:
    $o0 = "byte_40CD48" wide ascii nocase
    $o1 = "byte_411A30" wide ascii nocase
    $o2 = "doexit" wide ascii nocase
    $o3 = "GetSystemTime" wide ascii nocase
  condition:
    4 of ($o*)
}