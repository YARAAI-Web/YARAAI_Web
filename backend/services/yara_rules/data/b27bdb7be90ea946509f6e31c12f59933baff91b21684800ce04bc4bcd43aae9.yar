rule auto_rule_20250726192558_7288 {
  strings:
    $o0 = "dword_1400FF828" wide ascii nocase
    $o1 = "dword_1400FF55C" wide ascii nocase
  condition:
    all of them
}