rule auto_rule_20250727040951_7295 {
  strings:
    $o0 = "off_100D37F8" wide ascii nocase
    $o1 = "winWrite2" wide ascii nocase
  condition:
    all of them
}