rule auto_rule_20250726211805_7987 {
  strings:
    $o0 = "off_4293C8" wide ascii nocase
    $o1 = "x2623" wide ascii nocase
    $o2 = "xEC8EE3C2" wide ascii nocase
    $o3 = "hwndParenta" wide ascii nocase
  condition:
    4 of ($o*)
}