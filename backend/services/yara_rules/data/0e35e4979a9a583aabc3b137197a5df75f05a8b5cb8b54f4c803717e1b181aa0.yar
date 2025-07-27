rule auto_rule_20250726145250_1369 {
  strings:
    $o0 = "x7510856" wide ascii nocase
    $o1 = "ReplaceTextW" wide ascii nocase
    $o2 = "SetLayout" wide ascii nocase
  condition:
    3 of ($o*)
}