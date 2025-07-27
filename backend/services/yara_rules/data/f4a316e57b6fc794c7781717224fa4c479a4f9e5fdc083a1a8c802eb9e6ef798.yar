rule auto_rule_20250727040213_7615 {
  strings:
    $o0 = "byte_411640" wide ascii nocase
    $o1 = "xcptlookup" wide ascii nocase
  condition:
    all of them
}