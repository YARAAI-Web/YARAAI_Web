rule auto_rule_20250726194742_7517 {
  strings:
    $o0 = "x404A7B" wide ascii nocase
    $o1 = "LocalLock" wide ascii nocase
  condition:
    all of them
}