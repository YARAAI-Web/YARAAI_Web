rule auto_rule_20250726183854_1394 {
  strings:
    $o0 = "aQcapDll" wide ascii nocase
  condition:
    all of them
}