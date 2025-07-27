rule auto_rule_20250726175817_8691 {
  strings:
    $o0 = "memcpy_0" wide ascii nocase
    $o1 = "UnwindUp5_0" wide ascii nocase
    $o2 = "VirtualLock" wide ascii nocase
  condition:
    3 of ($o*)
}