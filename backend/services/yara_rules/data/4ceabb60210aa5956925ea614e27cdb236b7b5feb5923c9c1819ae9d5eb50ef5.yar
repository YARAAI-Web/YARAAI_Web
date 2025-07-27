rule auto_rule_20250726151551_9300 {
  strings:
    $o0 = "lpBuf1" wide ascii nocase
    $o1 = "lpdwCount" wide ascii nocase
  condition:
    all of them
}