rule auto_rule_20250726192336_0117 {
  strings:
    $o0 = "_cpinfo" wide ascii nocase
    $o1 = "Origin" wide ascii nocase
    $o2 = "aInconsistentIo" wide ascii nocase
    $o3 = "Debug" wide ascii nocase
  condition:
    4 of ($o*)
}