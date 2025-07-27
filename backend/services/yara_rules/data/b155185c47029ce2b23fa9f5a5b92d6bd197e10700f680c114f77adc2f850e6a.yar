rule auto_rule_20250727014138_0284 {
  strings:
    $o0 = "__readgsqword" wide ascii nocase
  condition:
    all of them
}