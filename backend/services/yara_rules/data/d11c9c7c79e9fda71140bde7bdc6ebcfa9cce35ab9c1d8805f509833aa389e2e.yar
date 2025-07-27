rule auto_rule_20250726082423_6684 {
  strings:
    $o0 = "dword_45D8B8" wide ascii nocase
    $o1 = "dword_45D3C8" wide ascii nocase
  condition:
    all of them
}