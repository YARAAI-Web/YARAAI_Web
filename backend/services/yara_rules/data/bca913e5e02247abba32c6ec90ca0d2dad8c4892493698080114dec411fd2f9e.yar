rule auto_rule_20250726132737_2274 {
  strings:
    $o0 = "a1system32Cscri_0" wide ascii nocase
    $o1 = "lstrcatW" wide ascii nocase
  condition:
    all of them
}