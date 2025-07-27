rule auto_rule_20250726094005_4743 {
  strings:
    $o0 = "PtVisible" wide ascii nocase
    $o1 = "x8D79" wide ascii nocase
  condition:
    all of them
}