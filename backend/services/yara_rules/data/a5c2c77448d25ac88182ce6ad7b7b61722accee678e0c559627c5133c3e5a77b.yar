rule auto_rule_20250726062841_9105 {
  strings:
    $o0 = "dwInfoType" wide ascii nocase
    $o1 = "byte_45D580" wide ascii nocase
    $o2 = "TrailDown2" wide ascii nocase
  condition:
    3 of ($o*)
}