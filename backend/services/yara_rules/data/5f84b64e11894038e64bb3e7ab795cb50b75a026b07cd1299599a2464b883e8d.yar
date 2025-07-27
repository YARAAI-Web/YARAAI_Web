rule auto_rule_20250726072117_6389 {
  strings:
    $o0 = "dword_7822C" wide ascii nocase
    $o1 = "HighPoolPriority" wide ascii nocase
  condition:
    all of them
}