rule auto_rule_20250726164554_9321 {
  strings:
    $o0 = "dword_469090" wide ascii nocase
    $o1 = "_pLastBlock" wide ascii nocase
    $o2 = "NumberOfEventsRead" wide ascii nocase
  condition:
    3 of ($o*)
}