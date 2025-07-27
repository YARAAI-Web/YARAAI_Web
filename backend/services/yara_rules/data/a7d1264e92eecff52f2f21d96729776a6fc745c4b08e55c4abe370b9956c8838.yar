rule auto_rule_20250726144554_4612 {
  strings:
    $o0 = "dword_407938" wide ascii nocase
    $o1 = "dword_40787C" wide ascii nocase
  condition:
    all of them
}