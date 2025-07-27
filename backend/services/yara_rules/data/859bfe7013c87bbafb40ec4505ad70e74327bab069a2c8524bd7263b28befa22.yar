rule auto_rule_20250726205958_2931 {
  strings:
    $o0 = "UnwindUp4_0" wide ascii nocase
    $o1 = "_set_errno" wide ascii nocase
    $o2 = "dword_47E068" wide ascii nocase
  condition:
    3 of ($o*)
}