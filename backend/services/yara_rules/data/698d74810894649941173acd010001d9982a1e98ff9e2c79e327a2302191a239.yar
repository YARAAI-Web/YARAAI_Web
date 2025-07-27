rule auto_rule_20250726182452_9660 {
  strings:
    $o0 = "EF4h" wide ascii nocase
    $o1 = "x64000000" wide ascii nocase
  condition:
    all of them
}