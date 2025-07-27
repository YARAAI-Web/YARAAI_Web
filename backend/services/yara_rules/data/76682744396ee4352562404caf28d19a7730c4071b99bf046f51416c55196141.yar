rule auto_rule_20250727000045_4150 {
  strings:
    $o0 = "lpfn" wide ascii nocase
    $o1 = "dword_79F70C" wide ascii nocase
  condition:
    all of them
}