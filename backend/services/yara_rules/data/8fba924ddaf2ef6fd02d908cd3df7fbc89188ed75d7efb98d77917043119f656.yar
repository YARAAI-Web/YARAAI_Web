rule auto_rule_20250727003540_2937 {
  strings:
    $o0 = "ShowCursor" wide ascii nocase
    $o1 = "dword_40AD04" wide ascii nocase
    $o2 = "TargetHandle" wide ascii nocase
  condition:
    3 of ($o*)
}