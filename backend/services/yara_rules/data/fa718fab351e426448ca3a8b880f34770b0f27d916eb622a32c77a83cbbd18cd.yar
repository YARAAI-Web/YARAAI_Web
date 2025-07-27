rule auto_rule_20250726215315_8732 {
  strings:
    $o0 = "x70941FD1" wide ascii nocase
    $o1 = "x1248" wide ascii nocase
    $o2 = "xE68u" wide ascii nocase
  condition:
    3 of ($o*)
}