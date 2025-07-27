rule auto_rule_20250726181636_6609 {
  strings:
    $o0 = "_heap_init" wide ascii nocase
    $o1 = "byte_4757BC" wide ascii nocase
    $o2 = "dword_475930" wide ascii nocase
    $o3 = "off_4751FC" wide ascii nocase
    $o4 = "GdipDeleteBrush" wide ascii nocase
  condition:
    4 of ($o*)
}