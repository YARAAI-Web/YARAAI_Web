rule auto_rule_20250726133025_2181 {
  strings:
    $o0 = "byte_64028F54" wide ascii nocase
    $o1 = "u_long" wide ascii nocase
  condition:
    all of them
}