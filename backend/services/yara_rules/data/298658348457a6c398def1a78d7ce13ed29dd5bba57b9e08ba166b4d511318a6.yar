rule auto_rule_20250726141954_4583 {
  strings:
    $o0 = "TrailDown1_0" wide ascii nocase
    $o1 = "_msize" wide ascii nocase
    $o2 = "VisualC" wide ascii nocase
    $o3 = "dword_41A018" wide ascii nocase
    $o4 = "UnwindUp0_0" wide ascii nocase
  condition:
    5 of ($o*)
}