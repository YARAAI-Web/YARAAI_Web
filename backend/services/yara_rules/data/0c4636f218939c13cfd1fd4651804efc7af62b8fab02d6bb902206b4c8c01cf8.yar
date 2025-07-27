rule auto_rule_20250727030757_6791 {
  strings:
    $o0 = "dword_44E5F8" wide ascii nocase
    $o1 = "nProgram" wide ascii nocase
    $o2 = "GdipDeleteFontFamily" wide ascii nocase
    $o3 = "__shr_12" wide ascii nocase
  condition:
    4 of ($o*)
}