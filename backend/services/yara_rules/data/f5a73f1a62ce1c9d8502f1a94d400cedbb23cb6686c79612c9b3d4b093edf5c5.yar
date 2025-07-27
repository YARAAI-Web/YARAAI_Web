rule auto_rule_20250727031154_2787 {
  strings:
    $o0 = "ppsEditable" wide ascii nocase
  condition:
    all of them
}