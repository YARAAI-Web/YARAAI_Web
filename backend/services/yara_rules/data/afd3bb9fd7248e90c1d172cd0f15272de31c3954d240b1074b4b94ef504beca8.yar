rule auto_rule_20250726101400_0086 {
  strings:
    $o0 = "_CrtMemCheckPoint" wide ascii nocase
    $o1 = "byte_446D00" wide ascii nocase
  condition:
    all of them
}