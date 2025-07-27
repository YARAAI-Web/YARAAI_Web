rule auto_rule_20250726152049_9849 {
  strings:
    $o0 = "off_6C7AE4" wide ascii nocase
    $o1 = "off_6C7A34" wide ascii nocase
  condition:
    all of them
}