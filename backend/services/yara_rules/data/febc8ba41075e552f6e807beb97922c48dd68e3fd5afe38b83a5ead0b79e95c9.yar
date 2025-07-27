rule auto_rule_20250726235622_2804 {
  strings:
    $o0 = "x110" wide ascii nocase
    $o1 = "x4AB6" wide ascii nocase
  condition:
    all of them
}