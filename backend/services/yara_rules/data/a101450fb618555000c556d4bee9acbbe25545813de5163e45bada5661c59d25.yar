rule auto_rule_20250726182023_8851 {
  strings:
    $o0 = "off_42E18B" wide ascii nocase
    $o1 = "x244ECBDAu" wide ascii nocase
  condition:
    all of them
}