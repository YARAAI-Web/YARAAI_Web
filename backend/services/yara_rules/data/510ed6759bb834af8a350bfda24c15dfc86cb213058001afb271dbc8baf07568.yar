rule auto_rule_20250726064428_3335 {
  strings:
    $o0 = "GetMenuBarInfo" wide ascii nocase
    $o1 = "bRedraw" wide ascii nocase
    $o2 = "DrawEdge" wide ascii nocase
    $o3 = "x17000u" wide ascii nocase
  condition:
    4 of ($o*)
}