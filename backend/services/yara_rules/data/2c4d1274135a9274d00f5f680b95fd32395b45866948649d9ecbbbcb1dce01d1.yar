rule auto_rule_20250727042629_2862 {
  strings:
    $o0 = "dword_406078" wide ascii nocase
    $o1 = "x4080200u" wide ascii nocase
  condition:
    all of them
}