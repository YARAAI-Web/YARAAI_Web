rule auto_rule_20250726213601_6835 {
  strings:
    $o0 = "off_4679D0" wide ascii nocase
    $o1 = "dwInfoType" wide ascii nocase
  condition:
    all of them
}