rule auto_rule_20250726204155_1467 {
  strings:
    $o0 = "nBlockUse" wide ascii nocase
    $o1 = "Runtime" wide ascii nocase
    $o2 = "stream" wide ascii nocase
  condition:
    3 of ($o*)
}