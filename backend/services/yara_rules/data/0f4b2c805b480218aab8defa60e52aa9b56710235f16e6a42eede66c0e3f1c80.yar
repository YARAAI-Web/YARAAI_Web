rule auto_rule_20250726092218_8633 {
  strings:
    $o0 = "off_45650C" wide ascii nocase
    $o1 = "strcat" wide ascii nocase
  condition:
    all of them
}