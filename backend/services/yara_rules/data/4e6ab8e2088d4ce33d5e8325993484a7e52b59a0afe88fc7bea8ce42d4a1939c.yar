rule auto_rule_20250726171255_9977 {
  strings:
    $o0 = "x48F7u" wide ascii nocase
    $o1 = "dwInQueue" wide ascii nocase
    $o2 = "x22F2u" wide ascii nocase
    $o3 = "dword_42A018" wide ascii nocase
  condition:
    4 of ($o*)
}