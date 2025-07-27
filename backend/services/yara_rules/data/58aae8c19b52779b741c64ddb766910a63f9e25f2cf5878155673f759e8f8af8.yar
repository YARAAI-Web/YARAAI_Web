rule auto_rule_20250726100113_0298 {
  strings:
    $o0 = "TrailDown2" wide ascii nocase
    $o1 = "dword_446010" wide ascii nocase
    $o2 = "TrailDown1_0" wide ascii nocase
  condition:
    3 of ($o*)
}