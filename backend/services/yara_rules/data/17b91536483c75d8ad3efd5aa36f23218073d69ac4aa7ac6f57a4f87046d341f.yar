rule auto_rule_20250726183201_6695 {
  strings:
    $o0 = "dword_468558" wide ascii nocase
    $o1 = "off_408680" wide ascii nocase
  condition:
    all of them
}