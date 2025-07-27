rule auto_rule_20250726181435_0781 {
  strings:
    $o0 = "algn_475BF2" wide ascii nocase
    $o1 = "x3FBFu" wide ascii nocase
  condition:
    all of them
}