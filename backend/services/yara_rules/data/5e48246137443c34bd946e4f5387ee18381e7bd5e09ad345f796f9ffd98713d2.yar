rule auto_rule_20250726133744_6370 {
  strings:
    $o0 = "dword_42B1EE" wide ascii nocase
    $o1 = "x3AFA003272F5LL" wide ascii nocase
    $o2 = "dword_42B20E" wide ascii nocase
  condition:
    3 of ($o*)
}