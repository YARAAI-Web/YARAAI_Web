rule auto_rule_20250726135135_6010 {
  strings:
    $o0 = "off_403004" wide ascii nocase
    $o1 = "lstrcatA" wide ascii nocase
  condition:
    all of them
}