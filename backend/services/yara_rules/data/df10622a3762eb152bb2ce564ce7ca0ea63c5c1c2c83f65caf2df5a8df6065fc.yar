rule auto_rule_20250727033823_1934 {
  strings:
    $o0 = "fdwClose" wide ascii nocase
    $o1 = "__shl_12" wide ascii nocase
  condition:
    all of them
}