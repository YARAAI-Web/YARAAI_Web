rule auto_rule_20250726161350_5632 {
  strings:
    $o0 = "byte_3F682190" wide ascii nocase
    $o1 = "debugstatssystem" wide ascii nocase
  condition:
    all of them
}