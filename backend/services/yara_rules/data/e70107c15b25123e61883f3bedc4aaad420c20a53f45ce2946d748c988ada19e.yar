rule auto_rule_20250726203420_5231 {
  strings:
    $o0 = "_NLG_Notify" wide ascii nocase
    $o1 = "dword_44C4E4" wide ascii nocase
    $o2 = "dword_44B550" wide ascii nocase
    $o3 = "copy_start" wide ascii nocase
    $o4 = "TrailDown0" wide ascii nocase
  condition:
    4 of ($o*)
}