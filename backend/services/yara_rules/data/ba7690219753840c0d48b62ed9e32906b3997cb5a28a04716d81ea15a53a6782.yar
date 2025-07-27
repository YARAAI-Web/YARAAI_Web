rule auto_rule_20250726192407_9012 {
  strings:
    $o0 = "fnCallback" wide ascii nocase
    $o1 = "_nh_malloc_dbg" wide ascii nocase
    $o2 = "byte_460F48" wide ascii nocase
    $o3 = "Sourcea" wide ascii nocase
  condition:
    4 of ($o*)
}