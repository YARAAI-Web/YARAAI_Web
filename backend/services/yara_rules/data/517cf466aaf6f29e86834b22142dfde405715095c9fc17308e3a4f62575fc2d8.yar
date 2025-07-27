rule auto_rule_20250727041009_4961 {
  strings:
    $o0 = "_abnormal_termination" wide ascii nocase
    $o1 = "UnwindUp3_0" wide ascii nocase
    $o2 = "dword_45C440" wide ascii nocase
    $o3 = "dword_45CF08" wide ascii nocase
  condition:
    4 of ($o*)
}