rule auto_rule_20250726094311_7155 {
  strings:
    $o0 = "x40DF" wide ascii nocase
    $o1 = "xFA5E15E2" wide ascii nocase
    $o2 = "x41B3DE" wide ascii nocase
    $o3 = "x3DBEu" wide ascii nocase
    $o4 = "GetDateFormatA" wide ascii nocase
  condition:
    4 of ($o*)
}