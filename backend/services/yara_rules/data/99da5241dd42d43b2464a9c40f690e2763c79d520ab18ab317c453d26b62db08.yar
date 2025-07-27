rule auto_rule_20250727020116_8551 {
  strings:
    $o0 = "GetSysColorBrush" wide ascii nocase
    $o1 = "lpsa" wide ascii nocase
    $o2 = "lpAccelDst" wide ascii nocase
  condition:
    3 of ($o*)
}