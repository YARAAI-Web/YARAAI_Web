rule auto_rule_20250726231525_7780 {
  strings:
    $o0 = "x1A3Fu" wide ascii nocase
    $o1 = "x3544u" wide ascii nocase
    $o2 = "dword_42B000" wide ascii nocase
    $o3 = "szShortPath" wide ascii nocase
  condition:
    4 of ($o*)
}