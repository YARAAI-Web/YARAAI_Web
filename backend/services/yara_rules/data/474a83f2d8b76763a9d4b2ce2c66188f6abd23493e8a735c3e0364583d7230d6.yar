rule auto_rule_20250726120848_4054 {
  strings:
    $o0 = "_byte_0" wide ascii nocase
    $o1 = "byte_411D94" wide ascii nocase
    $o2 = "strncnt" wide ascii nocase
  condition:
    3 of ($o*)
}