rule auto_rule_20250726201504_3707 {
  strings:
    $o0 = "DevCapsA" wide ascii nocase
    $o1 = "VisualC" wide ascii nocase
    $o2 = "off_474A6C" wide ascii nocase
    $o3 = "off_47520C" wide ascii nocase
  condition:
    4 of ($o*)
}