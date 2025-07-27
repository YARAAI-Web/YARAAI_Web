rule auto_rule_20250726065509_6755 {
  strings:
    $o0 = "off_455CE8" wide ascii nocase
    $o1 = "off_45647C" wide ascii nocase
  condition:
    all of them
}