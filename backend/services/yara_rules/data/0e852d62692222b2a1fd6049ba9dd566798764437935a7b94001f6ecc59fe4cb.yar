rule auto_rule_20250727015208_0853 {
  strings:
    $o0 = "dword_465544" wide ascii nocase
    $o1 = "dodwords" wide ascii nocase
  condition:
    all of them
}