rule auto_rule_20250726142045_9846 {
  strings:
    $o0 = "dword_4118FC" wide ascii nocase
    $o1 = "__sbh_heap_init" wide ascii nocase
    $o2 = "dword_40E004" wide ascii nocase
    $o3 = "dword_411D64" wide ascii nocase
  condition:
    4 of ($o*)
}