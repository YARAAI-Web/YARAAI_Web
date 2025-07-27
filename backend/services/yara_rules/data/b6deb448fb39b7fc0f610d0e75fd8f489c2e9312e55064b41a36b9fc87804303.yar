rule auto_rule_20250726115901_8116 {
  strings:
    $o0 = "off_402014" wide ascii nocase
  condition:
    all of them
}