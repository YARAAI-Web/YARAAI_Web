rule auto_rule_20250726154310_7303 {
  strings:
    $o0 = "off_44DD1C" wide ascii nocase
  condition:
    all of them
}