rule auto_rule_20250726130638_1404 {
  strings:
    $o0 = "x180000014LL" wide ascii nocase
    $o1 = "dword_18000C764" wide ascii nocase
    $o2 = "x180008468LL" wide ascii nocase
  condition:
    3 of ($o*)
}