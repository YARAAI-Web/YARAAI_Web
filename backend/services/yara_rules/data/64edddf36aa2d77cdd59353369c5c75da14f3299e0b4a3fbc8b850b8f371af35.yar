rule auto_rule_20250726230804_2128 {
  strings:
    $o0 = "CopyIcon" wide ascii nocase
    $o1 = "uSizeStruct" wide ascii nocase
    $o2 = "QueueUserAPC" wide ascii nocase
    $o3 = "DdeFreeDataHandle" wide ascii nocase
  condition:
    4 of ($o*)
}