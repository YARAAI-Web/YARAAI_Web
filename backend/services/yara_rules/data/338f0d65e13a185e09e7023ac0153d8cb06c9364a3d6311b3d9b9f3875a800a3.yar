rule auto_rule_20250726092513_0842 {
  strings:
    $o0 = "UnwindUp4_0" wide ascii nocase
    $o1 = "dword_44C8E4" wide ascii nocase
    $o2 = "TrailUp0_0" wide ascii nocase
    $o3 = "icebp" wide ascii nocase
  condition:
    4 of ($o*)
}