rule auto_rule_20250726112620_8311 {
  strings:
    $o0 = "OpenIcon" wide ascii nocase
    $o1 = "x64FCu" wide ascii nocase
    $o2 = "pbmih" wide ascii nocase
    $o3 = "x4904" wide ascii nocase
  condition:
    4 of ($o*)
}