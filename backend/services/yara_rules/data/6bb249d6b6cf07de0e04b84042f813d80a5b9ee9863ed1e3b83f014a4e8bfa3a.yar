rule auto_rule_20250726223811_8797 {
  strings:
    $o0 = "off_45C914" wide ascii nocase
    $o1 = "_nh_malloc" wide ascii nocase
  condition:
    all of them
}