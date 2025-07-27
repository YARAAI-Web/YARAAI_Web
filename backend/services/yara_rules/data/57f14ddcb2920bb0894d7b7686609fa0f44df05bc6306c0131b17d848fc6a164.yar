rule auto_rule_20250727015700_8202 {
  strings:
    $o0 = "_flushall" wide ascii nocase
    $o1 = "_CrtMemCheckpoint" wide ascii nocase
    $o2 = "_except_handler3" wide ascii nocase
  condition:
    3 of ($o*)
}