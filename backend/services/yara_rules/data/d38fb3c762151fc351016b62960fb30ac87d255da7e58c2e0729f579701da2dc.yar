rule auto_rule_20250726190626_9376 {
  strings:
    $o0 = "TargetIp" wide ascii nocase
    $o1 = "dword_45CF0C" wide ascii nocase
    $o2 = "dword_45CDC0" wide ascii nocase
  condition:
    3 of ($o*)
}