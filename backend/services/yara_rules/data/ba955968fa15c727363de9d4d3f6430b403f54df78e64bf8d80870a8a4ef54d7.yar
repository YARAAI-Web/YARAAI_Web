rule auto_rule_20250726235047_3047 {
  strings:
    $o0 = "x40Bu" wide ascii nocase
    $o1 = "x2EB1u" wide ascii nocase
    $o2 = "x8A30" wide ascii nocase
    $o3 = "x7AE0u" wide ascii nocase
    $o4 = "hBrush" wide ascii nocase
  condition:
    4 of ($o*)
}