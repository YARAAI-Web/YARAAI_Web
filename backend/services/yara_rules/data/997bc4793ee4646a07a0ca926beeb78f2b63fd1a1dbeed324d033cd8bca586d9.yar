rule auto_rule_20250726220644_7649 {
  strings:
    $o0 = "dword_42B008" wide ascii nocase
    $o1 = "dword_45D2D4" wide ascii nocase
    $o2 = "dword_45DADC" wide ascii nocase
    $o3 = "Program" wide ascii nocase
  condition:
    4 of ($o*)
}