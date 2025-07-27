rule auto_rule_20250726135501_3390 {
  strings:
    $o0 = "x140u" wide ascii nocase
    $o1 = "x41C4u" wide ascii nocase
    $o2 = "dword_45D2D4" wide ascii nocase
    $o3 = "_NLG_Notify1" wide ascii nocase
    $o4 = "FileA" wide ascii nocase
  condition:
    5 of ($o*)
}