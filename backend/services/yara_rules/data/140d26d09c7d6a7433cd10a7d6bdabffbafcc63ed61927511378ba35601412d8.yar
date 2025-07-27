rule auto_rule_20250726151343_2187 {
  strings:
    $o0 = "x1DB3u" wide ascii nocase
    $o1 = "off_42E7E5" wide ascii nocase
  condition:
    all of them
}