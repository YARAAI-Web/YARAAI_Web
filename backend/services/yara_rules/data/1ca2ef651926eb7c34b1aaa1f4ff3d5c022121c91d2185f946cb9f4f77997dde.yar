rule auto_rule_20250726165903_8996 {
  strings:
    $o0 = "off_402014" wide ascii nocase
  condition:
    all of them
}