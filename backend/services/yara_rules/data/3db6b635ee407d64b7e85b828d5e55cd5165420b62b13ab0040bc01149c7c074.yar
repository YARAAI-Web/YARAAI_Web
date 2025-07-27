rule auto_rule_20250727024539_9329 {
  strings:
    $o0 = "dword_782BC" wide ascii nocase
    $o1 = "Executive" wide ascii nocase
  condition:
    all of them
}