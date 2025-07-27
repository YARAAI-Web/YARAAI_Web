rule auto_rule_20250726083317_5188 {
  strings:
    $o0 = "dword_44A04C" wide ascii nocase
    $o1 = "UnwindUp2_0" wide ascii nocase
    $o2 = "TrailDown2" wide ascii nocase
    $o3 = "dword_44A038" wide ascii nocase
  condition:
    4 of ($o*)
}