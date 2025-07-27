rule auto_rule_20250726154618_5301 {
  strings:
    $o0 = "off_42753C" wide ascii nocase
    $o1 = "dword_427E54" wide ascii nocase
  condition:
    all of them
}