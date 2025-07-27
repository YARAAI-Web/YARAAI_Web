rule auto_rule_20250726123507_9878 {
  strings:
    $o0 = "g_fnStartTransport" wide ascii nocase
    $o1 = "xFF00u" wide ascii nocase
  condition:
    all of them
}