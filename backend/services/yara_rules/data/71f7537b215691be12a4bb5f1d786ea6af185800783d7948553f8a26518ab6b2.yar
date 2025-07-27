rule auto_rule_20250727014159_1457 {
  strings:
    $o0 = "byte_45CF20" wide ascii nocase
    $o1 = "off_45C90C" wide ascii nocase
  condition:
    all of them
}