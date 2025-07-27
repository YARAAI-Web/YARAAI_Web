rule auto_rule_20250726140546_7417 {
  strings:
    $o0 = "off_455CE4" wide ascii nocase
  condition:
    all of them
}