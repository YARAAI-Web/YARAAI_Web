rule auto_rule_20250726190915_3548 {
  strings:
    $o0 = "dword_410994" wide ascii nocase
    $o1 = "VirtualFree" wide ascii nocase
    $o2 = "TrailUp0_0" wide ascii nocase
    $o3 = "dword_410580" wide ascii nocase
  condition:
    4 of ($o*)
}