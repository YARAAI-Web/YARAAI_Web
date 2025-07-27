rule auto_rule_20250726122753_3974 {
  strings:
    $o0 = "dword_463A20" wide ascii nocase
    $o1 = "dword_46549C" wide ascii nocase
    $o2 = "Sourcea" wide ascii nocase
  condition:
    3 of ($o*)
}