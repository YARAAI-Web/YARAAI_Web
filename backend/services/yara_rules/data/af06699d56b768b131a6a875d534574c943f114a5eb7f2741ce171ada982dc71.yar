rule auto_rule_20250726122030_4913 {
  strings:
    $o0 = "dword_4283CB" wide ascii nocase
    $o1 = "x3902u" wide ascii nocase
    $o2 = "x8E93D2A3" wide ascii nocase
  condition:
    3 of ($o*)
}