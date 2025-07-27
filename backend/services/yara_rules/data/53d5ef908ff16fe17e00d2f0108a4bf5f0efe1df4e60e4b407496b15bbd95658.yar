rule auto_rule_20250726235236_3594 {
  strings:
    $o0 = "dwCreationDisposition" wide ascii nocase
    $o1 = "off_4027E4" wide ascii nocase
  condition:
    all of them
}