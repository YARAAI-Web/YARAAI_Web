rule auto_rule_20250726161250_8328 {
  strings:
    $o0 = "lpSecurityAttributes" wide ascii nocase
    $o1 = "dword_413C84" wide ascii nocase
  condition:
    all of them
}