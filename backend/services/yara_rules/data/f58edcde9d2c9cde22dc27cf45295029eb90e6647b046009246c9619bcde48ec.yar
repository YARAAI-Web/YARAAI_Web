rule auto_rule_20250727042425_3532 {
  strings:
    $o0 = "_global_unwind2" wide ascii nocase
    $o1 = "_CrtMemCheckPoint" wide ascii nocase
  condition:
    all of them
}