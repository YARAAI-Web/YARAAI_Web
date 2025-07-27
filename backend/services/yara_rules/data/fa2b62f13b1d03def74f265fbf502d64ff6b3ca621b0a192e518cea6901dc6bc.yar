rule auto_rule_20250726064017_2144 {
  strings:
    $o0 = "fccHandler" wide ascii nocase
  condition:
    all of them
}