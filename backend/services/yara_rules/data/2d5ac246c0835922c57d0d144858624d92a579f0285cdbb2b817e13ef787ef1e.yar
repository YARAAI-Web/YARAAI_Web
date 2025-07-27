rule auto_rule_20250726205508_1442 {
  strings:
    $o0 = "dword_476C14" wide ascii nocase
  condition:
    all of them
}