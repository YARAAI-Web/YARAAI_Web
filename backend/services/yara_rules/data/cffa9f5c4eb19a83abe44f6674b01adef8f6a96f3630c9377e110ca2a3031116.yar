rule auto_rule_20250726065520_0590 {
  strings:
    $o0 = "RtlUnwind" wide ascii nocase
    $o1 = "off_44D570" wide ascii nocase
  condition:
    all of them
}