rule auto_rule_20250726191000_1577 {
  strings:
    $o0 = "TrailDown1_0" wide ascii nocase
    $o1 = "GdipDeleteBrush" wide ascii nocase
    $o2 = "UnwindUp6_0" wide ascii nocase
    $o3 = "fdwReset" wide ascii nocase
  condition:
    4 of ($o*)
}