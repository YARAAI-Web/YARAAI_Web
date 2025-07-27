rule auto_rule_20250727022115_5080 {
  strings:
    $o0 = "wFlags" wide ascii nocase
    $o1 = "ICRemove" wide ascii nocase
  condition:
    all of them
}