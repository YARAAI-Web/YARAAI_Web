rule auto_rule_20250726202332_5634 {
  strings:
    $o0 = "dword_449AD4" wide ascii nocase
    $o1 = "_abnormal_termination" wide ascii nocase
    $o2 = "Runtime" wide ascii nocase
    $o3 = "dword_407004" wide ascii nocase
    $o4 = "strncnt" wide ascii nocase
  condition:
    5 of ($o*)
}