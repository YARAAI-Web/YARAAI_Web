rule auto_rule_20250727012643_6189 {
  strings:
    $o0 = "TrailDown1_0" wide ascii nocase
    $o1 = "GdipCreateFromHDC" wide ascii nocase
    $o2 = "BeginUpdateResourceA" wide ascii nocase
  condition:
    3 of ($o*)
}