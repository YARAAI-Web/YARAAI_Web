rule auto_rule_20250726181122_2713 {
  strings:
    $o0 = "off_469678" wide ascii nocase
  condition:
    all of them
}