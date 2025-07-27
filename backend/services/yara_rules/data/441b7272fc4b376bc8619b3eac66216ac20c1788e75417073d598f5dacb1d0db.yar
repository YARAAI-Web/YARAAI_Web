rule auto_rule_20250726182129_6746 {
  strings:
    $o0 = "hConvList" wide ascii nocase
    $o1 = "lpmi" wide ascii nocase
  condition:
    all of them
}