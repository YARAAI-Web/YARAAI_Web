rule auto_rule_20250726134155_1369 {
  strings:
    $o0 = "dword_404638" wide ascii nocase
    $o1 = "DefWindowProcA" wide ascii nocase
    $o2 = "DrawTextA" wide ascii nocase
  condition:
    3 of ($o*)
}