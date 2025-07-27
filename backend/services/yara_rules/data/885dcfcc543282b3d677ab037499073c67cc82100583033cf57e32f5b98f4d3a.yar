rule auto_rule_20250726120714_7239 {
  strings:
    $o0 = "byte_64029044" wide ascii nocase
    $o1 = "byte_64028E6C" wide ascii nocase
  condition:
    all of them
}