rule auto_rule_20250726110709_8899 {
  strings:
    $o0 = "lEnd" wide ascii nocase
    $o1 = "dword_46E008" wide ascii nocase
  condition:
    all of them
}