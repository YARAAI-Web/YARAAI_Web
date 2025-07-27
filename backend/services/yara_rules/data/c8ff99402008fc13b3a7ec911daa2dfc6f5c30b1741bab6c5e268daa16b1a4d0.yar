rule auto_rule_20250726234146_9882 {
  strings:
    $o0 = "dword_45CB04" wide ascii nocase
    $o1 = "tionAndSpinCount" wide ascii nocase
    $o2 = "dword_45CF0C" wide ascii nocase
  condition:
    3 of ($o*)
}