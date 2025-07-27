rule auto_rule_20250726093759_6229 {
  strings:
    $o0 = "_CrtDumpMemoryLeaks" wide ascii nocase
  condition:
    all of them
}