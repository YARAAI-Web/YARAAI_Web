rule auto_rule_20250727040154_2985 {
  strings:
    $o0 = "off_417F2C" wide ascii nocase
  condition:
    all of them
}