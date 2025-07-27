rule auto_rule_20250726154300_0621 {
  strings:
    $o0 = "dword_420F6C" wide ascii nocase
    $o1 = "x54E0u" wide ascii nocase
  condition:
    all of them
}