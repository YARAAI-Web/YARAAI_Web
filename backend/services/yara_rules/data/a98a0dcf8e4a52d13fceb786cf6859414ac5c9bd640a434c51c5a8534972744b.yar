rule auto_rule_20250726224357_8220 {
  strings:
    $o0 = "FindWindowExW" wide ascii nocase
    $o1 = "x37D8" wide ascii nocase
    $o2 = "usage" wide ascii nocase
    $o3 = "x84A" wide ascii nocase
  condition:
    4 of ($o*)
}