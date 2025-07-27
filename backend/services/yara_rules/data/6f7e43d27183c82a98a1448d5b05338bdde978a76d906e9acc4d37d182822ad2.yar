rule auto_rule_20250727005138_0260 {
  strings:
    $o0 = "memcpy_0" wide ascii nocase
    $o1 = "DeleteTimerQueue" wide ascii nocase
    $o2 = "_abnormal_termination" wide ascii nocase
    $o3 = "acmDriverDetailsA" wide ascii nocase
  condition:
    4 of ($o*)
}