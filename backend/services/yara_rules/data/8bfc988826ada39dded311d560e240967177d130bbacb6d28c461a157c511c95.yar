rule auto_rule_20250726070224_8785 {
  strings:
    $o0 = "TrailDown2" wide ascii nocase
    $o1 = "dword_411E30" wide ascii nocase
    $o2 = "dword_411F68" wide ascii nocase
  condition:
    3 of ($o*)
}