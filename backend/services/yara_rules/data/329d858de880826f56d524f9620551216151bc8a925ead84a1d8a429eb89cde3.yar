rule auto_rule_20250727034201_3714 {
  strings:
    $o0 = "quarter" wide ascii nocase
    $o1 = "VirtualAllocEx" wide ascii nocase
  condition:
    all of them
}