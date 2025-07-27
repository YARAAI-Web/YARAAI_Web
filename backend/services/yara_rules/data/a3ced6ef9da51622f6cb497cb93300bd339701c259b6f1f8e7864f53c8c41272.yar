rule auto_rule_20250726100125_8331 {
  strings:
    $o0 = "_CrtMemDumpAllObjectsSince" wide ascii nocase
    $o1 = "before" wide ascii nocase
  condition:
    all of them
}