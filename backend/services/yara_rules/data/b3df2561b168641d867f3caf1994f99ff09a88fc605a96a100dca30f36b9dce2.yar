rule auto_rule_20250726170723_6828 {
  strings:
    $o0 = "UnwindUp0_0" wide ascii nocase
    $o1 = "_NLG_Notify" wide ascii nocase
    $o2 = "dword_411E68" wide ascii nocase
    $o3 = "dword_411970" wide ascii nocase
  condition:
    4 of ($o*)
}