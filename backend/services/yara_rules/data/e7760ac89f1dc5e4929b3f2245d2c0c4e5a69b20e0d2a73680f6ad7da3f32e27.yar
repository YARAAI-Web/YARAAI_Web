rule auto_rule_20250726144015_8680 {
  strings:
    $o0 = "xF89C853B" wide ascii nocase
    $o1 = "x5DA3u" wide ascii nocase
  condition:
    all of them
}