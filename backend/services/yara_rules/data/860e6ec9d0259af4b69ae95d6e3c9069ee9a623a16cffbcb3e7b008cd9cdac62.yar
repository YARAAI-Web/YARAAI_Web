rule auto_rule_20250726134738_4389 {
  strings:
    $o0 = "UnwindUp3_0" wide ascii nocase
    $o1 = "dword_467328" wide ascii nocase
    $o2 = "xtoa" wide ascii nocase
    $o3 = "VisualC" wide ascii nocase
  condition:
    4 of ($o*)
}