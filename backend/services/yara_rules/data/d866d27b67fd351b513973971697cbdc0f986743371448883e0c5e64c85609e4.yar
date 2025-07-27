rule auto_rule_20250726174237_9822 {
  strings:
    $o0 = "x163Cu" wide ascii nocase
    $o1 = "dword_420F70" wide ascii nocase
  condition:
    all of them
}