rule auto_rule_20250726212819_9437 {
  strings:
    $o0 = "off_49DDB8" wide ascii nocase
    $o1 = "d250m0" wide ascii nocase
    $o2 = "d5m0" wide ascii nocase
  condition:
    3 of ($o*)
}