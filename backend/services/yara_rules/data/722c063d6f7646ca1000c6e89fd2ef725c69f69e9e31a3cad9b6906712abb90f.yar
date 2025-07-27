rule auto_rule_20250726074343_4397 {
  strings:
    $o0 = "dword_4336E7" wide ascii nocase
    $o1 = "dword_433717" wide ascii nocase
    $o2 = "x3241u" wide ascii nocase
  condition:
    3 of ($o*)
}