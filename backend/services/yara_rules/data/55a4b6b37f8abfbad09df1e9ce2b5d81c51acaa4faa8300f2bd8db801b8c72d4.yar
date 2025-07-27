rule auto_rule_20250726151835_9375 {
  strings:
    $o0 = "dword_6502E060" wide ascii nocase
    $o1 = "j__free" wide ascii nocase
  condition:
    all of them
}