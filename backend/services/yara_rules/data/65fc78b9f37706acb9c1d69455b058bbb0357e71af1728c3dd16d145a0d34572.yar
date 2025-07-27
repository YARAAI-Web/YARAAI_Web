rule auto_rule_20250727042254_0764 {
  strings:
    $o0 = "g_fnStartTransport" wide ascii nocase
  condition:
    all of them
}