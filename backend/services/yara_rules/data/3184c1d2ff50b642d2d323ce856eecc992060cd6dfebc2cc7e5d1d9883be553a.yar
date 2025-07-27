rule auto_rule_20250726230510_0656 {
  strings:
    $o0 = "x7D59u" wide ascii nocase
    $o1 = "GetCommModemStatus" wide ascii nocase
  condition:
    all of them
}