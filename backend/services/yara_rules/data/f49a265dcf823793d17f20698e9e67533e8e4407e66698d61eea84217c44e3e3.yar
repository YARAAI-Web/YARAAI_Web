rule auto_rule_20250727011611_2456 {
  strings:
    $o0 = "dword_45D3F8" wide ascii nocase
    $o1 = "TrailDown1_0" wide ascii nocase
    $o2 = "_cpinfo" wide ascii nocase
  condition:
    3 of ($o*)
}