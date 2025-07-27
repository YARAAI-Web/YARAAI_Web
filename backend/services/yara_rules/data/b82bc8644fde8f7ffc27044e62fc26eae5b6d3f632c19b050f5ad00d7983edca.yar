rule auto_rule_20250726170326_9447 {
  strings:
    $o0 = "dwFlagsAndAttributes" wide ascii nocase
    $o1 = "bErase" wide ascii nocase
    $o2 = "aNdvnnn32" wide ascii nocase
  condition:
    3 of ($o*)
}