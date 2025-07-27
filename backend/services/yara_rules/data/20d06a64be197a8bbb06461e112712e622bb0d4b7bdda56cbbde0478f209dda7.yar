rule auto_rule_20250726143240_7457 {
  strings:
    $o0 = "TrailDown2" wide ascii nocase
    $o1 = "MaxCharCount" wide ascii nocase
    $o2 = "dword_463D84" wide ascii nocase
    $o3 = "dword_4647B4" wide ascii nocase
    $o4 = "_cpinfo" wide ascii nocase
  condition:
    4 of ($o*)
}