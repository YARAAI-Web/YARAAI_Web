rule auto_rule_20250726195254_7322 {
  strings:
    $o0 = "x8A85" wide ascii nocase
    $o1 = "x3609u" wide ascii nocase
    $o2 = "x2447u" wide ascii nocase
    $o3 = "OutBuffer" wide ascii nocase
  condition:
    4 of ($o*)
}