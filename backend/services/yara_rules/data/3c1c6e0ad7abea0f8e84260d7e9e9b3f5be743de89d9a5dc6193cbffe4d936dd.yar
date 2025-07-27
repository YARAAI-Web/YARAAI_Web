rule auto_rule_20250726205039_5285 {
  strings:
    $o0 = "dword_4011EC" wide ascii nocase
    $o1 = "RegOpenKeyA" wide ascii nocase
  condition:
    all of them
}