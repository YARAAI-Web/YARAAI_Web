rule auto_rule_20250726173659_9143 {
  strings:
    $o0 = "dword_476AEC" wide ascii nocase
    $o1 = "dword_476FAC" wide ascii nocase
  condition:
    all of them
}