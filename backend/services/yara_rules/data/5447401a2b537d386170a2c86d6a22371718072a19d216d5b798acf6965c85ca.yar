rule auto_rule_20250726065405_9052 {
  strings:
    $o0 = "x22C088" wide ascii nocase
    $o1 = "ExFreePoolWithTag" wide ascii nocase
  condition:
    all of them
}