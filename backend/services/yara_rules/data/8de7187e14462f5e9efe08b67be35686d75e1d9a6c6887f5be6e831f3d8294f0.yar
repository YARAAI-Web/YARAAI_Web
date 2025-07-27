rule auto_rule_20250726071842_3501 {
  strings:
    $o0 = "off_40251C" wide ascii nocase
  condition:
    all of them
}