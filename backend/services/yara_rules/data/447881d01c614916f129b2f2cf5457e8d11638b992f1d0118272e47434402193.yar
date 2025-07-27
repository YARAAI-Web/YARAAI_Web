rule auto_rule_20250726065015_5753 {
  strings:
    $o0 = "x423DA5" wide ascii nocase
    $o1 = "dword_465D10" wide ascii nocase
  condition:
    all of them
}