rule auto_rule_20250726114847_0611 {
  strings:
    $o0 = "dword_40E018" wide ascii nocase
    $o1 = "x140u" wide ascii nocase
    $o2 = "TrailDown0_0" wide ascii nocase
    $o3 = "dword_411970" wide ascii nocase
  condition:
    4 of ($o*)
}