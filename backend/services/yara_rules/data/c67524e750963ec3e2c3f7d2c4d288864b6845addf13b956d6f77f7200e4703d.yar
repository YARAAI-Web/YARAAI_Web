rule auto_rule_20250726185555_8538 {
  strings:
    $o0 = "wLanguage" wide ascii nocase
    $o1 = "lpBytesPerSector" wide ascii nocase
    $o2 = "lpScrollRectangle" wide ascii nocase
    $o3 = "DrawCaption" wide ascii nocase
    $o4 = "NumberOfPages" wide ascii nocase
  condition:
    4 of ($o*)
}