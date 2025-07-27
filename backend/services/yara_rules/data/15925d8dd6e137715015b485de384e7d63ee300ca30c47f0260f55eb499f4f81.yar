rule auto_rule_20250727001747_0606 {
  strings:
    $o0 = "_CrtCheckMemory" wide ascii nocase
  condition:
    all of them
}