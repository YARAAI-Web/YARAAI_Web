rule auto_rule_20250726064907_9086 {
  strings:
    $o0 = "dword_4673BC" wide ascii nocase
    $o1 = "_aullrem" wide ascii nocase
    $o2 = "dword_40F018" wide ascii nocase
  condition:
    3 of ($o*)
}