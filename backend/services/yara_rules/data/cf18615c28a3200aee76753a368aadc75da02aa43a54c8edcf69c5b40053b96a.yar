rule auto_rule_20250726121754_6214 {
  strings:
    $o0 = "aNegopenkeyw" wide ascii nocase
    $o1 = "lstrcatW" wide ascii nocase
  condition:
    all of them
}