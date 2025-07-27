rule auto_rule_20250727014129_4991 {
  strings:
    $o0 = "mixerSetControlDetails" wide ascii nocase
  condition:
    all of them
}