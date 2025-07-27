rule auto_rule_20250726121139_9155 {
  strings:
    $o0 = "dword_462018" wide ascii nocase
    $o1 = "dump" wide ascii nocase
    $o2 = "x101" wide ascii nocase
    $o3 = "__endstdio" wide ascii nocase
  condition:
    4 of ($o*)
}