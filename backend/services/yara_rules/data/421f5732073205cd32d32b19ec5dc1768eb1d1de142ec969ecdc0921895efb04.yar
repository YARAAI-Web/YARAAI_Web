rule auto_rule_20250726223150_6088 {
  strings:
    $o0 = "xAEDD4D18" wide ascii nocase
  condition:
    all of them
}