rule auto_rule_20250726075634_7843 {
  strings:
    $o0 = "dword_467E90" wide ascii nocase
    $o1 = "DrawDibSetPalette" wide ascii nocase
  condition:
    all of them
}