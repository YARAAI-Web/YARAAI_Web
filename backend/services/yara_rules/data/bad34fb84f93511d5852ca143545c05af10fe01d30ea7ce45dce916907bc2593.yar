rule auto_rule_20250726193700_0317 {
  strings:
    $o0 = "xA4D" wide ascii nocase
    $o1 = "dword_4D316C" wide ascii nocase
  condition:
    all of them
}