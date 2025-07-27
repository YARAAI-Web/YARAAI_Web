rule auto_rule_20250726231422_1462 {
  strings:
    $o0 = "dword_44E96C" wide ascii nocase
    $o1 = "GdipCreateFontFamilyFromName" wide ascii nocase
  condition:
    all of them
}