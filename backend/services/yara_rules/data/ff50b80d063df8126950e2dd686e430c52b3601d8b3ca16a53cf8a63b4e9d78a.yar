rule auto_rule_20250726073233_3266 {
  strings:
    $o0 = "x707B" wide ascii nocase
  condition:
    all of them
}