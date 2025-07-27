rule auto_rule_20250726133827_0072 {
  strings:
    $o0 = "GdipCreateSolidFill" wide ascii nocase
    $o1 = "_cropzeros" wide ascii nocase
    $o2 = "off_44D854" wide ascii nocase
    $o3 = "dword_44EB24" wide ascii nocase
  condition:
    4 of ($o*)
}