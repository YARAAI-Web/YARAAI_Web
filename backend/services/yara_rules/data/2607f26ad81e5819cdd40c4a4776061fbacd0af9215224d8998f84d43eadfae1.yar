rule auto_rule_20250726102851_2185 {
  strings:
    $o0 = "aBxn2y3j0lmrsba" wide ascii nocase
  condition:
    all of them
}