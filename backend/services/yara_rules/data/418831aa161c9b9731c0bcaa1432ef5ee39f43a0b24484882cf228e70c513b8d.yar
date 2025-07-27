rule auto_rule_20250726221106_9168 {
  strings:
    $o0 = "_itoa" wide ascii nocase
    $o1 = "dword_468034" wide ascii nocase
    $o2 = "_flushall" wide ascii nocase
    $o3 = "_heapchk" wide ascii nocase
  condition:
    4 of ($o*)
}