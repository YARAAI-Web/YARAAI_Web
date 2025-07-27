rule auto_rule_20250726154704_0975 {
  strings:
    $o0 = "off_44D578" wide ascii nocase
  condition:
    all of them
}