rule auto_rule_20250726205543_3054 {
  strings:
    $o0 = "off_44E024" wide ascii nocase
  condition:
    all of them
}