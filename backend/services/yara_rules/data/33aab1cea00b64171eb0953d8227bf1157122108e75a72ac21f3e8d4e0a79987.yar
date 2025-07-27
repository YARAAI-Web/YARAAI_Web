rule auto_rule_20250726183535_0504 {
  strings:
    $o0 = "x2695" wide ascii nocase
    $o1 = "dword_40D454" wide ascii nocase
  condition:
    all of them
}