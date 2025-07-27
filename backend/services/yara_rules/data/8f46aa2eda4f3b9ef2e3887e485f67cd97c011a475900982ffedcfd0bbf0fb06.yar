rule auto_rule_20250727040317_1364 {
  strings:
    $o0 = "off_47941C" wide ascii nocase
    $o1 = "cause" wide ascii nocase
  condition:
    all of them
}