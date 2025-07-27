rule auto_rule_20250726115146_4285 {
  strings:
    $o0 = "lpNumberOfBytesWritten" wide ascii nocase
    $o1 = "wsprintfA" wide ascii nocase
    $o2 = "aNdvnnn32" wide ascii nocase
  condition:
    3 of ($o*)
}