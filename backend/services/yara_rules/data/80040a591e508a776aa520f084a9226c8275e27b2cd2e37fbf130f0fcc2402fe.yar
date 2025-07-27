rule auto_rule_20250726231903_8215 {
  strings:
    $o0 = "x403671" wide ascii nocase
    $o1 = "x140u" wide ascii nocase
  condition:
    all of them
}