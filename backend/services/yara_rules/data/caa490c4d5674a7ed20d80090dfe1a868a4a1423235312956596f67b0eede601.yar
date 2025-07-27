rule auto_rule_20250726111734_3189 {
  strings:
    $o0 = "_mtdeletelocks" wide ascii nocase
    $o1 = "_nh_malloc" wide ascii nocase
    $o2 = "off_45C91C" wide ascii nocase
    $o3 = "TrailDown1" wide ascii nocase
  condition:
    4 of ($o*)
}