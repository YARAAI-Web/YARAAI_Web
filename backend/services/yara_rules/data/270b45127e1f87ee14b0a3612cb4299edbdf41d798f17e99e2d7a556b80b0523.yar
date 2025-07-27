rule auto_rule_20250726234917_4127 {
  strings:
    $o0 = "TrailDown1_0" wide ascii nocase
    $o1 = "dword_40BE30" wide ascii nocase
    $o2 = "dword_40B548" wide ascii nocase
    $o3 = "UnwindUp2_0" wide ascii nocase
  condition:
    4 of ($o*)
}